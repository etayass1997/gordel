from flask import Flask, render_template, request, jsonify, Response
import ipaddress
import os
import re
import secrets
import socket
import requests
from urllib.parse import urlparse

# This service delegates all model work to knowledge-agent.
os.environ.pop('ANTHROPIC_API_KEY', None)

app = Flask(__name__)
# No CORS: the frontend is served by this same Flask app (same-origin), so the
# API needs no cross-origin access. Enabling it would let any third-party site
# call these endpoints from a visitor's browser and burn API quota/cost.

def _load_env(name, default=''):
    # Try environment variable first, then a local .env file (dev convenience)
    value = os.environ.get(name, '')
    if value:
        return value
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(env_path):
        for line in open(env_path, encoding='utf-8', errors='ignore').read().splitlines():
            if line.startswith(f'{name}='):
                return line.split('=', 1)[1].strip()
    return default

# Optional HTTP Basic Auth gate (set GORDEL_PASSWORD to enable). Without it,
# the app is unauthenticated and, once exposed publicly, would let anyone
# with the URL burn API quota on this account.
AUTH_USER = _load_env('GORDEL_USER', 'gordel')
AUTH_PASSWORD = _load_env('GORDEL_PASSWORD')
KNOWLEDGE_AGENT_URL = _load_env('KNOWLEDGE_AGENT_URL', 'http://127.0.0.1:5066').rstrip('/')
KNOWLEDGE_AGENT_API_KEY = _load_env('KNOWLEDGE_AGENT_API_KEY')


@app.before_request
def _require_auth():
    if not AUTH_PASSWORD:
        return
    auth = request.authorization
    valid = bool(auth) and secrets.compare_digest(auth.username or '', AUTH_USER) \
        and secrets.compare_digest(auth.password or '', AUTH_PASSWORD)
    if not valid:
        return Response(
            'Authentication required', 401,
            {'WWW-Authenticate': 'Basic realm="Gordel"'}
        )

from rag_engine import RAGEngine
rag = RAGEngine()

SYSTEM_TROUBLESHOOT = """אתה גורדל — סוכן טכני מומחה לכלי צמה ומכונות בנייה כבדות.

## תפקידך
אתה עוזר למפעילי כלי צמה לאבחן תקלות מכניות ולקבל הנחיות תיקון ברורות בעברית.

## כלי צמה שאתה מכיר
מחפרונים (Excavators), בולדוזרים (Bulldozers), מטענים/לודרים (Loaders), גרירות (Graders), מדחסים (Compactors), עגורנים (Cranes).
יצרנים: קטרפילר (CAT), קובלקו, היטאצ'י, קוואטסו, וולוו, ליברהר, JCB, קייס.

## תמונות
המפעיל עשוי לצרף תמונה (למשל קופסת פיוזים, לוח מחוונים, נורית תקלה, רכיב שדורש זיהוי, קוד שגיאה על מסך, נזל, או חלק פיזי). כאשר מצורפת תמונה:
• תאר בקצרה מה אתה מזהה בתמונה לפני שאתה עונה.
• אם רואים קופסת פיוזים — ציין אם ניתן לזהות תוויות/מספרים, ושאל לפרטים נוספים אם התווית לא קריאה בבירור.
• אם רואים נורית אזהרה/קוד תקלה — פרש את הסימן/קוד לפי הידע שלך ביצרני הכלי.
• אם התמונה לא קשורה לכלי צמה או לא ברורה מספיק לאבחון, אמור זאת בפירוש ובקש תמונה נוספת או תיאור.

## פורמט תשובה
**סיכום:** [משפט אחד על התקלה]

**מקורות אפשריים:**
• [מקור 1] — [הסבר + הסתברות]
• [מקור 2] — [הסבר]

**צעדי בדיקה:**
1. [צעד ראשון]
2. [צעד שני]
...

**⚠️ אזהרה:** [רק אם יש סכנה בטיחותית - לחץ, חום, נפילת ציוד]"""

SYSTEM_VISUALIZE = """אתה גורדל — מומחה לכלי צמה.
תן הנחיות החלפת רכיב מפורטות בעברית.

## פורמט:
**כלים נדרשים:** [רשימה]

**אמצעי בטיחות:**
• [אמצעי 1]

**שלבי פירוק:**
1. ...

**שלבי התקנה:**
1. ...

**בדיקות לאחר ההחלפה:**
1. ..."""


@app.route('/')
def index():
    return render_template('index.html')


_DATA_URL_RE = re.compile(r'^data:(image/(?:jpeg|png|gif|webp));base64,(.+)$', re.DOTALL)
_MAX_IMAGE_BYTES = 8 * 1024 * 1024  # 8MB raw image data
_MAX_QUESTION_CHARS = 4000


def _parse_image(data_url):
    """Parse a data: URL into (media_type, base64_data), or raise ValueError."""
    m = _DATA_URL_RE.match(data_url.strip())
    if not m:
        raise ValueError('פורמט תמונה לא נתמך (יש להשתמש ב-JPEG/PNG/GIF/WEBP)')
    media_type, b64data = m.group(1), m.group(2)
    if len(b64data) * 3 / 4 > _MAX_IMAGE_BYTES:
        raise ValueError('התמונה גדולה מדי (מקסימום 8MB)')
    return media_type, b64data


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    question = str(data.get('question', '')).strip()
    image = str(data.get('image', '')).strip()
    if not question and not image:
        return jsonify({'error': 'שאלה ריקה'}), 400
    if len(question) > _MAX_QUESTION_CHARS:
        return jsonify({'error': f'שאלה ארוכה מדי (מקסימום {_MAX_QUESTION_CHARS} תווים)'}), 400

    content = []
    if image:
        try:
            media_type, b64data = _parse_image(image)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        content.append({
            'type': 'image',
            'source': {'type': 'base64', 'media_type': media_type, 'data': b64data}
        })

    search_text = question or 'נתח את התמונה המצורפת וזהה תקלה אפשרית'
    context = ''
    if rag.count() > 0:
        results = rag.search(search_text, n=4)
        docs = results.get('documents', [[]])[0]
        if docs:
            context = '\n\n---\n\n'.join(docs)

    user_msg = f"שאלה: {search_text}" if question else "המפעיל צירף תמונה ללא טקסט — נתח אותה וזהה תקלה אפשרית."
    if context:
        user_msg += f"\n\nמידע רלוונטי מבסיס הידע:\n{context}"
    else:
        user_msg += "\n\n(אין מידע ספציפי בבסיס הידע — ענה מהידע הכללי שלך)"

    content.append({'type': 'text', 'text': user_msg})

    contexts = [
        {'title': 'בסיס הידע של גורדל', 'source': 'gordel', 'content': doc}
        for doc in (docs if context else [])
    ]
    headers = {'X-API-Key': KNOWLEDGE_AGENT_API_KEY} if KNOWLEDGE_AGENT_API_KEY else {}
    try:
        upstream = requests.post(
            f'{KNOWLEDGE_AGENT_URL}/api/agents/base/chat',
            json={'question': search_text, 'contexts': contexts, 'image': image or None},
            headers=headers, timeout=(5, 240)
        )
        upstream.raise_for_status()
        payload = upstream.json()
        return jsonify({'answer': payload['answer'], 'kb_used': bool(context),
                        'provider': 'knowledge-agent', 'model': payload.get('model')})
    except (requests.RequestException, ValueError, KeyError) as e:
        return jsonify({'error': f'שירות knowledge-agent אינו זמין: {e}'}), 502


@app.route('/api/visualize', methods=['POST'])
def visualize():
    data = request.get_json(silent=True) or {}
    query = str(data.get('query', '')).strip()
    if not query:
        return jsonify({'error': 'שאילתה ריקה'}), 400
    if len(query) > _MAX_QUESTION_CHARS:
        return jsonify({'error': f'שאילתה ארוכה מדי (מקסימום {_MAX_QUESTION_CHARS} תווים)'}), 400

    _BROWSER_UA = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    )
    images = []
    web_text = ''
    try:
        from duckduckgo_search import DDGS
        with DDGS(headers={'User-Agent': _BROWSER_UA, 'Accept-Language': 'en-US,en;q=0.9'}) as ddgs:
            img_results = list(ddgs.images(
                f"{query} excavator heavy equipment part diagram repair",
                max_results=8, safesearch='moderate'
            ))
            images = [{'url': r['image'], 'title': r.get('title', '')} for r in img_results[:6]]

            text_results = list(ddgs.text(
                f"{query} replacement repair procedure steps heavy equipment",
                max_results=4
            ))
            web_text = '\n'.join(r.get('body', '') for r in text_results)
    except Exception:
        pass

    contexts = ([{'title': 'מידע עזר מהאינטרנט', 'source': 'gordel-web',
                  'content': web_text[:4000]}] if web_text else [])
    headers = {'X-API-Key': KNOWLEDGE_AGENT_API_KEY} if KNOWLEDGE_AGENT_API_KEY else {}
    try:
        upstream = requests.post(
            f'{KNOWLEDGE_AGENT_URL}/api/agents/base/chat',
            json={'question': f'תן מדריך בטיחותי ומפורט להחלפת: {query}', 'contexts': contexts},
            headers=headers, timeout=(5, 240)
        )
        upstream.raise_for_status()
        guide = upstream.json()['answer']
    except (requests.RequestException, ValueError, KeyError) as e:
        return jsonify({'error': f'שירות knowledge-agent אינו זמין: {e}'}), 502
    return jsonify({'guide': guide, 'images': images})


def _is_public_url(url):
    """Reject non-http(s) schemes and URLs resolving to private/loopback/link-local
    addresses, to prevent server-side request forgery via the KB-add endpoint."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https') or not parsed.hostname:
            return False
        for family, _, _, _, sockaddr in socket.getaddrinfo(parsed.hostname, None):
            ip = ipaddress.ip_address(sockaddr[0])
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
                return False
        return True
    except (ValueError, socket.gaierror):
        return False


@app.route('/api/kb/add', methods=['POST'])
def add_to_kb():
    data = request.get_json(silent=True) or {}
    url = str(data.get('url', '')).strip()
    if not url:
        return jsonify({'error': 'כתובת URL ריקה'}), 400
    if not _is_public_url(url):
        return jsonify({'error': 'כתובת URL לא חוקית או לא נגישה'}), 400
    try:
        from scraper import scrape_url
        text, title = scrape_url(url)
        if len(text) < 100:
            return jsonify({'error': 'תוכן הדף קצר מדי'}), 400
        doc_id = ''.join(c for c in url if c.isalnum())[-50:]
        rag.add_document(text, {'source': url, 'title': title, 'topic': 'web'}, doc_id)
        return jsonify({'success': True, 'title': title, 'chars': len(text)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/kb/stats')
def kb_stats():
    return jsonify({'count': rag.count()})


@app.route('/api/kb/seed', methods=['POST'])
def seed_kb_route():
    from seed_kb import seed_knowledge_base
    count = seed_knowledge_base(rag)
    return jsonify({'seeded': count})


if __name__ == '__main__':
    if rag.count() == 0:
        print("Seeding knowledge base...")
        from seed_kb import seed_knowledge_base
        seed_knowledge_base(rag)
    port = int(os.environ.get('PORT', 5003))
    print(f"Gordel running on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
