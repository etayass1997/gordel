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
| 22/07/2026 | סקירת קוד: תיקוני אבטחה (הסרת CORS פתוח, הגנת SSRF ב-`/api/kb/add`, XSS בתצוגת תמונות, טעינת JSON בטוחה בנתיבי ה-API), הסרת נתיב מקומי קשיח מ-`_load_api_key`, תיקון קישור "סקר שוק" שהצביע ל-localhost |
| 28/06/2026 | הוספת Liebherr KB (`add_liebherr_kb.py`) |
| 28/06/2026 | הוספת Hitachi KB (`add_hitachi_kb.py`) |
| 28/06/2026 | הוספת Manitou KB (`add_manitou_kb.py`) |
| 28/06/2026 | עדכון `kb_data.json` + `Procfile` |
| 19/06/2026 | תיקוני app.py ו-templates |
| 16/06/2026 | הקמת הפרויקט, seed KB, scraper |

## עתידי / פתוח
- [x] KB ל-Komatsu — קיים כבר ב-`add_kb_batch.py` (הרשומה למעלה הייתה לא מעודכנת)
- [ ] KB ל-Case — עדיין חסר (רק אזכורי "Case Drain" הידראוליים לא קשורים)
- [ ] מחירי שוק (market pricing) — לממש בפועל; הכפתור "פתח סוכן סקר שוק" מבוטל זמנית (הצביע ל-localhost)
- [ ] דפלוי Render בפועל
