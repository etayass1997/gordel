# גורדל — סוכן אבחון כלי צמה כבדה

## תיאור
סוכן AI לאבחון תקלות מכניות בכלי צמה ומכונות בנייה כבדות. עונה בעברית עם ניתוח תמונה (קופסת פיוזים, לוח מחוונים, קוד תקלה) ומחירי שוק. מבוסס BM25 RAG על KB יצרנים מרובים.

## סטאק
- **Backend**: Flask (Python), port 5003
- **RAG**: BM25 מקומי (`rag_engine.py`) + ChromaDB
- **AI**: Anthropic Claude (Vision + טקסט)
- **Frontend**: HTML/CSS/JS ב-`templates/`
- **דפלוי**: Render

## יצרנים נתמכים
CAT, Kobelco, Hitachi, Komatsu, Volvo, Liebherr, JCB, Case, Doosan, Manitou

## קבצים מרכזיים
| קובץ | תפקיד |
|------|--------|
| `app.py` | Flask backend + system prompt גורדל |
| `rag_engine.py` | BM25 engine |
| `seed_kb.py` | אתחול KB |
| `add_*_kb.py` | הוספת ידע ליצרן ספציפי |
| `add_general_systems_kb.py` | ידע כללי חוצה-יצרנים (מיזוג, בלמים, מצברים, צמיגים, DEF/SCR, טלמטיקה, חורף, שימון) |
| `kb_data.json` | מאגר ידע מאוחד |
| `scraper.py` | שאיבת מידע ליצרנים |

## הרצה מקומית
```bash
pip install -r requirements.txt
set ANTHROPIC_API_KEY=sk-ant-...
python app.py   # http://localhost:5003
```

## System Prompt
גורדל מזהה תמונות, מפרש קודי תקלה, מנחה לתיקון עם סיכום + מקורות אפשריים + הוראות שלב-שלב.
