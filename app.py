from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import anthropic
import base64
import os
import re

app = Flask(__name__)
CORS(app)

def _load_api_key():
    # Try environment variable first, then .env file
    key = os.environ.get('ANTHROPIC_API_KEY', '')
    if key:
        return key
    env_path = r'C:\Users\User\עבודה\.env'
    if os.path.exists(env_path):
        for line in open(env_path, encoding='utf-8', errors='ignore').read().splitlines():
            if line.startswith('ANTHROPIC_API_KEY='):
                return line.split('=', 1)[1].strip()
    raise RuntimeError('ANTHROPIC_API_KEY not found')

API_KEY = _load_api_key()
client = anthropic.Anthropic(api_key=API_KEY)

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
    data = request.json
    question = data.get('question', '').strip()
    image = data.get('image', '').strip()
    if not question and not image:
        return jsonify({'error': 'שאלה ריקה'}), 400

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

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=SYSTEM_TROUBLESHOOT,
        messages=[{"role": "user", "content": content}]
    )
    return jsonify({'answer': response.content[0].text, 'kb_used': bool(context)})


@app.route('/api/visualize', methods=['POST'])
def visualize():
    data = request.json
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'error': 'שאילתה ריקה'}), 400

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

    prompt = f"כיצד מחליפים: {query}\n\n"
    if web_text:
        prompt += f"מידע מהאינטרנט:\n{web_text[:2000]}"

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=SYSTEM_VISUALIZE,
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({'guide': response.content[0].text, 'images': images})


@app.route('/api/kb/add', methods=['POST'])
def add_to_kb():
    data = request.json
    url = data.get('url', '').strip()
    if not url:
        return jsonify({'error': 'כתובת URL ריקה'}), 400
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
