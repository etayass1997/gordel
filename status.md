# גורדל — סטטוס פרויקט

## סטטוס כללי: ✅ פעיל + KB בהרחבה מתמדת

## מה הושלם
- [x] Flask backend + BM25 RAG engine
- [x] ChromaDB ל-vector storage
- [x] KB בסיסי: CAT, JCB, Volvo, Doosan, Kobelco (hitachi)
- [x] תמיכה בתמונות (Vision API)
- [x] System prompt גורדל — פורמט תשובה מובנה
- [x] Frontend (templates)
- [x] `render.yaml` + `Procfile`
- [x] אייקוני PWA (`generate_icons.py`)
- [x] `.gitignore`

## שינויים אחרונים
| תאריך | שינוי |
|--------|-------|
| 21/07/2026 | הוספת ידע כללי חוצה-יצרנים: מיזוג/HVAC, בלמים, מצברים והתנעה, צמיגים/זחלילים, DEF/SCR, טלמטיקה, הפעלה בקור, שימון (`add_general_systems_kb.py`, 249→274 chunks) |
| 28/06/2026 | הוספת Liebherr KB (`add_liebherr_kb.py`) |
| 28/06/2026 | הוספת Hitachi KB (`add_hitachi_kb.py`) |
| 28/06/2026 | הוספת Manitou KB (`add_manitou_kb.py`) |
| 28/06/2026 | עדכון `kb_data.json` + `Procfile` |
| 19/06/2026 | תיקוני app.py ו-templates |
| 16/06/2026 | הקמת הפרויקט, seed KB, scraper |

## עתידי / פתוח
- [ ] KB לKomatsu
- [ ] KB לCase
- [ ] מחירי שוק (market pricing) — לממש
- [ ] דפלוי Render בפועל
