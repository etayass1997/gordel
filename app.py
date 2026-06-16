from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import anthropic
import os

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


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': 'שאלה ריקה'}), 400

    context = ''
    if rag.count() > 0:
        results = rag.search(question, n=4)
        docs = results.get('documents', [[]])[0]
        if docs:
            context = '\n\n---\n\n'.join(docs)

    user_msg = f"שאלה: {question}"
    if context:
        user_msg += f"\n\nמידע רלוונטי מבסיס הידע:\n{context}"
    else:
        user_msg += "\n\n(אין מידע ספציפי בבסיס הידע — ענה מהידע הכללי שלך)"

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=SYSTEM_TROUBLESHOOT,
        messages=[{"role": "user", "content": user_msg}]
    )
    return jsonify({'answer': response.content[0].text, 'kb_used': bool(context)})


@app.route('/api/visualize', methods=['POST'])
def visualize():
    data = request.json
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'error': 'שאילתה ריקה'}), 400

    images = []
    web_text = ''
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
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
    app.run(host='0.0.0.0', port=port, debug=False)
