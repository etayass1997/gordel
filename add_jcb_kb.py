"""Add JCB knowledge base entries to Gordel."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

JCB_ENTRIES = [
    # ── New-wave agent: 19 entries ──────────────────────────────────────────
    {
        "id": "jcb_excavator_hydraulic_001",
        "text": (
            "תקלות הידראוליקה במחפרון JCB JS300 / JS370\n\n"
            "מחפרוני JCB JS300 ו-JS370 משתמשים במערכת הידראולית Load Sensing עם משאבת בוכנה משתנה (Variable Displacement Piston Pump).\n\n"
            "קוד שגיאה JCB LiveLink נפוץ: H-001 — לחץ הידראולי ראשי נמוך מתחת ל-280 bar.\n\n"
            "1. כל הפונקציות איטיות או חלשות\n"
            "   בדיקה: חבר מד לחץ ל-Test Port ליד הבלוק הראשי. ערך תקין: 320–350 bar בעומס מלא.\n"
            "   אם נמוך מ-280 bar: בדוק Main Relief Valve לכיוון נכון (350 bar).\n"
            "   פתרון: אם Relief תקין — בדוק Pump Flow Test — ירידה מ-15% = משאבה שחוקה.\n\n"
            "2. זרוע/בום יורדים כשמנוע כבוי (Cylinder Drift)\n"
            "   גורם: דליפה פנימית בגלינדרי הבום או ב-Load Hold Check Valve.\n"
            "   בדיקה: הצב בום גבוה, כבה מנוע — מד ירידה לאחר 5 דקות. מעל 20mm: החלף אטמי גלינדר.\n\n"
            "3. תנועה לא סמטרית בזרוע\n"
            "   גורם: Flow Divider פגום.\n"
            "   פתרון: ניקוי ובדיקת Flow Divider Block.\n\n"
            "תחזוקה מניעתית:\n"
            "שמן הידראולי (Shell Tellus S2 MX 46) — כל 2,000 שעות.\n"
            "פילטר הידראולי: כל 500 שעות. נקה Oil Cooler כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "JCB JS300,JCB JS370", "symptom": "לחץ הידראולי נמוך,תנועה איטית", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_powershift_001",
        "text": (
            "תיבת הילוכים Powershift במחפרת-טרקטור JCB 3CX / 4CX\n\n"
            "ה-JCB 3CX ו-4CX מצוידים בתיבת הילוכים Powershift אוטומטית.\n"
            "קוד שגיאה JCB LiveLink נפוץ: T-003 — לחץ Powershift Clutch נמוך.\n\n"
            "1. החלפת הילוך לא חלקה / 'בעיטה' בהחלפה\n"
            "   גורם: לחץ Clutch Pack נמוך מ-14 bar.\n"
            "   בדיקה: מד לחץ בפורט ה-Clutch Pack — ערך תקין: 16–18 bar.\n"
            "   פתרון: בדוק Transmission Filter — סתום = לחץ נמוך. החלף כל 500 שעות.\n\n"
            "2. כלי לא זז בהילוך קדימה/אחורה (No Drive)\n"
            "   בדוק: Neutral Start Switch — אם פגום, הבקר חושב שהגיר בניטרל.\n"
            "   בדוק: Solenoid Forward/Reverse עם וולטמטר (12V בהפעלה).\n"
            "   בדוק: Inching Pedal — אם תקוע = מנתק הנעה.\n\n"
            "3. שמן תיבת הילוכים מחומם יתר\n"
            "   קוד LiveLink: T-007.\n"
            "   פתרון: נקה Transmission Oil Cooler, בדוק זרימת קירור.\n\n"
            "4. רעש גריסה מתיבת ההילוכים\n"
            "   גורם: מחסור שמן ATF Dexron III/JCB HP Fluid.\n"
            "   המלצה: החלפת שמן כל 1,000 שעות.\n"
            "שמן Powershift: JCB HP Fluid — 18 ליטר ל-3CX, 22 ליטר ל-4CX."
        ),
        "metadata": {"source": "seed", "topic": "תיבת הילוכים,Powershift", "equipment": "JCB 3CX,JCB 4CX", "symptom": "החלפת הילוך לא חלקה,כלי לא זז", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_stabilizer_001",
        "text": (
            "תקלות מייצבים (Stabilizers) ב-JCB 3CX / 4CX\n\n"
            "ה-JCB 3CX ו-4CX מצוידים בארבעה מייצבים — שניים קדמיים (Slew) ושניים אחוריים.\n\n"
            "1. מייצב יורד לאט מאוד\n"
            "   גורם: Flow Control Valve מכוון נמוך, או דליפה בגלינדר.\n"
            "   פתרון: כיוון, או החלפת אטמי גלינדר (Stabilizer Cylinder Seal Kit).\n\n"
            "2. מייצב 'יורד מעצמו' תחת עומס — סכנה!\n"
            "   גורם: Counterbalance Valve פגום.\n"
            "   בדיקה: הרם מייצב, המתן 5 דקות — ירידה מעל 5mm = תקלה.\n"
            "   פתרון: החלף Counterbalance Valve.\n\n"
            "3. מייצב קדמי נטוי (Slew Stabilizer) לא מסתובב\n"
            "   גורם: Pivot Pin תקוע מחוסר שימון.\n"
            "   פתרון: שמן + גריז, אם עדיין תקוע — פרק ונקה ציר.\n\n"
            "4. נורת אזהרה מייצב דולקת\n"
            "   קוד LiveLink: S-011. גורם: חיישן מיקום (Position Sensor) לא מכוון.\n"
            "   פתרון: בדוק חיישן, כיוון, החלף אם נדרש.\n\n"
            "זיכרון בטיחות: לעולם אל תחפור ב-3CX/4CX כשהמייצבים לא נעולים."
        ),
        "metadata": {"source": "seed", "topic": "מייצבים,הידראוליקה", "equipment": "JCB 3CX,JCB 4CX", "symptom": "מייצב איטי,מייצב יורד", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_loader_arm_001",
        "text": (
            "תקלות זרוע מטען קדמי (Loader Arm) ב-JCB 3CX / 4CX\n\n"
            "1. זרוע מטען יורדת כשמנוע כבוי (Loader Arm Drift)\n"
            "   גורם: דליפה פנימית בגלינדרי ההרמה (Lift Cylinder Internal Leak).\n"
            "   בדיקה: הרם זרוע, כבה מנוע — ירידה מעל 25mm ב-5 דקות = החלפת אטמי גלינדר.\n\n"
            "2. כף מטען לא נועלת בזווית (Bucket Not Self-Leveling)\n"
            "   גורם: Self-Level Valve פגום.\n"
            "   פתרון: כיוון מחדש של Mechanical Self-Level Link, או תיקון שסתום.\n\n"
            "3. זרוע מטען לא מגיעה לגובה מלא\n"
            "   גורם: שסתום Relief של גלינדרי ההרמה מכוון נמוך מדי.\n"
            "   ערך תקין: 240–260 bar.\n\n"
            "4. רעש פטישים בירידת זרוע\n"
            "   גורם: Lowering Control / Regeneration Valve לא מכוון.\n\n"
            "5. כף מטען לא נפתחת/נסגרת\n"
            "   בדוק Bucket Tilt Cylinder לאטמים שחוקים.\n"
            "   בדוק שסתום Bucket Relief — 200–220 bar."
        ),
        "metadata": {"source": "seed", "topic": "זרוע מטען,הידראוליקה", "equipment": "JCB 3CX,JCB 4CX", "symptom": "זרוע יורדת,כף לא נועלת", "brand": "JCB"}
    },
    {
        "id": "jcb_telehandler_boom_001",
        "text": (
            "תקלות זרוע טלסקופית (Boom Extension) ב-JCB 540-170 / 535-125 / 531-70\n\n"
            "JCB 540-170: גובה הרמה 17 מטר. JCB 535-125: 12.5 מטר. JCB 531-70: 7 מטר.\n\n"
            "1. זרוע לא פותחת / פותחת לאט (Slow Telescope Extension)\n"
            "   גורם: שסתום Telescope Relief מכוון נמוך, או Slider Pads שחוקים.\n"
            "   בדיקה: לחץ Telescope — ערך תקין: 180–200 bar.\n"
            "   פתרון: בדוק ושנן Slider Pads, החלף אם שחוקים.\n\n"
            "2. זרוע 'נופלת' בסיום פתיחה\n"
            "   גורם: Telescope End Cushion Valve פגום.\n\n"
            "3. Carriage Tilt לא פועל בגובה מלא\n"
            "   קוד LiveLink: L-004 — Overload Warning. מערכת SCS/LMS חסמה.\n"
            "   פתרון: הורד גובה, בדוק Load Indicator.\n\n"
            "4. רעש חריקה בפתיחת זרוע\n"
            "   גורם: Slider Pads יבשים.\n"
            "   פתרון: שמן ב-JCB High Pressure Grease — כל 50 שעות.\n\n"
            "תחזוקה: שמן Slide Pads כל 50 שעות, Pivot Pins כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "זרוע טלסקופית,הידראוליקה", "equipment": "JCB 540-170,JCB 535-125,JCB 531-70", "symptom": "זרוע איטית,זרוע לא פותחת", "brand": "JCB"}
    },
    {
        "id": "jcb_telehandler_load_management_001",
        "text": (
            "מערכת ניהול עומסים (SCS / LMS) ב-Telehandler JCB\n\n"
            "מכונות JCB Telehandler מצוידות במערכת SCS (Stability Control System) למניעת פיכוח.\n\n"
            "קודי LiveLink:\n"
            "• L-001: עומס על גבול (Near Overload) — אזהרה.\n"
            "• L-002: עומס עבר גבול (Overload) — חסימת תנועת זרוע.\n"
            "• L-005: חיישן עומס (Load Cell) פגום.\n"
            "• L-008: חיישן זווית זרוע (Boom Angle Sensor) פגום.\n\n"
            "1. נורת עומס דולקת אדום ללא עומס\n"
            "   גורם: Load Cell מכוון לא נכון.\n"
            "   פתרון: כיול מחדש (Calibration) לפי הוראות JCB.\n\n"
            "2. מערכת חוסמת תנועה למרות עומס בטוח\n"
            "   גורם: Boom Angle Sensor שגוי.\n"
            "   פתרון: כיול Angle Sensor דרך JCB ServiceMaster 4.\n\n"
            "3. אזהרות SCS לא מופיעות\n"
            "   קוד: L-009. גורם: תקלת CAN Bus.\n\n"
            "בטיחות: לעולם לא לבטל SCS בעת עבודה.\n"
            "טבלת עומסים JCB 540-170: 0–5m: עד 4,000 ק\"ג. 5–10m: 2,500 ק\"ג. 10–17m: 1,000 ק\"ג."
        ),
        "metadata": {"source": "seed", "topic": "ניהול עומסים,SCS", "equipment": "JCB 540-170,JCB 535-125,JCB 531-70", "symptom": "עומס יתר,חסימת זרוע", "brand": "JCB"}
    },
    {
        "id": "jcb_mini_excavator_001",
        "text": (
            "תקלות מחפרון מיני JCB 8018 / 8055 / 8085\n\n"
            "מחפרוני המיני JCB (סדרת 8000) — ה-8018 (1.8 טון), 8055 (5.5 טון), 8085 (8.5 טון) — עם מנוע יאנמאר (Yanmar) ומערכת Gear Pump.\n\n"
            "1. כלי לא נוסע בכיוון אחד\n"
            "   גורם: Travel Motor אוטמים פגומים, או Travel Spool תקוע.\n"
            "   בדיקה: לחץ נסיעה שני הצדדים — צריך להיות שווה (~250 bar).\n\n"
            "2. Boom/Arm חלשים אחרי התחממות\n"
            "   גורם: Gear Pump שחוקה — יעילות יורדת עם טמפרטורה.\n"
            "   בדיקה: לחץ לאחר 30 דקות — אם יורד מ-200 bar = משאבה שחוקה.\n\n"
            "3. מנוע יאנמאר (Yanmar) לא עולה בקור\n"
            "   גורם: Glow Plugs שחוקים.\n"
            "   בדיקה: מד התנגדות — צריך 0.4–0.6 אוהם לכל נר.\n"
            "   פתרון: החלף Glow Plugs כל 2,000 שעות.\n\n"
            "4. Swing חלש ב-8018/8055\n"
            "   גורם: Swing Motor Seal שחוק.\n"
            "   פתרון: Swing Motor Seal Kit.\n\n"
            "דגשים: שמן מנוע Yanmar 15W-40 — כל 250 שעות. שמן הידראולי ISO VG 46.\n"
            "בדוק Rubber Track Tension — רצועות גומי!"
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,מנוע,נסיעה", "equipment": "JCB 8018,JCB 8055,JCB 8085", "symptom": "נסיעה חד צדדית,סיבוב חלש", "brand": "JCB"}
    },
    {
        "id": "jcb_js_swing_travel_001",
        "text": (
            "תקלות סיבוב (Swing) ונסיעה (Travel) ב-JCB JS300 / JS370\n\n"
            "מנגנון סיבוב JCB JS:\n\n"
            "1. סיבוב איטי מצד אחד\n"
            "   בדיקה: לחץ בפורטים L ו-R של Swing Motor — ערך תקין: 240–260 bar בשני הצדדים.\n"
            "   פתרון: כיוון Swing Relief Valves ל-250 bar.\n\n"
            "2. עצירה לא חלקה (Swing Doesn't Stop Smoothly)\n"
            "   גורם: Swing Anti-Reaction Valve פגום.\n"
            "   פתרון: החלף Anti-Reaction Valve על גוף Swing Motor.\n\n"
            "3. Swing Bearing רועש / רפוי\n"
            "   JS300/JS370: Swing Bearing קוטר ~1.2 מטר.\n"
            "   בדיקה: הנח זרוע על הקרקע, נסה להרים הבית — רפיון מעל 2mm = בדוק.\n"
            "   שימון: כל 250 שעות (LiveLink: SR-001).\n\n"
            "נסיעה:\n\n"
            "4. כלי לא הולך ישר (Steering Drift)\n"
            "   בדיקה: נסיעה 20 מטר — חריגה מעל 30cm = תקלה ב-Travel Motor.\n"
            "   לחץ Travel Left vs Right — שוני מעל 30 bar = תקלה.\n\n"
            "5. Parking Brake לא משתחרר\n"
            "   גורם: לחץ Pilot לא מגיע לשסתום — צריך 30–35 bar.\n\n"
            "6. רטט בנסיעה\n"
            "   בדוק: מתח זחל JS300: רפיון 25–35mm. בדוק שחיקת Sprocket ו-Track Links."
        ),
        "metadata": {"source": "seed", "topic": "סיבוב,נסיעה,הידראוליקה", "equipment": "JCB JS300,JCB JS370", "symptom": "סיבוב איטי,כלי לא הולך ישר", "brand": "JCB"}
    },
    {
        "id": "jcb_444_dieselmax_engine_001",
        "text": (
            "מנוע JCB 444 ו-Dieselmax — תקלות ואבחון\n\n"
            "JCB מייצרת מנועיה בעצמה — מנוע JCB 444 (4 צילינדרים, 4.4 ליטר) ו-JCB Dieselmax (6 צילינדרים).\n\n"
            "1. עשן שחור בהאצה\n"
            "   קוד LiveLink: E-037 — Injector Balance Fault.\n"
            "   גורם: Fuel Injectors עמידה לא אחידה, מסנן אוויר סתום, Turbocharger ירוד.\n"
            "   פתרון: ניקוי Injectors, כיול דרך JCB ServiceMaster 4.\n\n"
            "2. תאורת 'Engine Fault' (CEL) דולקת\n"
            "   קוד: E-044 — EGR Valve Stuck.\n"
            "   פתרון: נקה EGR Valve בממס מיוחד. אם פגום — החלף.\n\n"
            "3. לחץ שמן מנוע נמוך\n"
            "   קוד LiveLink: E-001 — Oil Pressure Critical. כבה מנוע מיד!\n"
            "   בדיקה: מפלס שמן תחילה. לחץ תקין: 3.5–4.5 bar בסרלנטי.\n\n"
            "4. רעש 'נקישה' מהמנוע\n"
            "   גורם: Injector Timing לא נכון, או Piston Pin Bearing שחוק.\n\n"
            "תחזוקה JCB 444:\n"
            "• שמן מנוע: JCB 10W-30 ACEA E9 — 13 ליטר. כל 500 שעות (Tier 4).\n"
            "• Timing Belt: החלפה כל 2,000 שעות — קריטי!"
        ),
        "metadata": {"source": "seed", "topic": "מנוע JCB 444", "equipment": "JCB 3CX,JCB 4CX,JCB JS300,JCB 540-170", "symptom": "עשן שחור,לחץ שמן נמוך,נקישה", "brand": "JCB"}
    },
    {
        "id": "jcb_livelink_fault_codes_001",
        "text": (
            "קודי שגיאה JCB LiveLink — מדריך שטח\n\n"
            "JCB LiveLink — מערכת ניטור ואבחון מובנית. כלי אבחון: JCB ServiceMaster 4.\n\n"
            "קודי שגיאה נפוצים:\n"
            "• E-037: Injector Balance Fault — ניקוי/החלפת Injector.\n"
            "• H-001: Main Hydraulic Pressure Low — בדוק Main Relief Valve, ספיקת משאבה.\n"
            "• T-003: Powershift Clutch Pressure Low (3CX/4CX) — בדוק Transmission Filter.\n"
            "• T-007: Transmission Oil Overheating — נקה Transmission Oil Cooler.\n"
            "• L-002: Telehandler Overload — הפחת עומס, בדוק Load Cell Calibration.\n"
            "• S-011: Stabilizer Sensor Fault (3CX/4CX) — בדוק חיישן, כיוון, החלף.\n"
            "• E-044: EGR Valve Position Fault — נקה EGR Valve.\n"
            "• SR-001: Swing Bearing Grease Low — הכנס גריז ל-Swing Bearing.\n\n"
            "שימוש ב-ServiceMaster 4:\n"
            "• חבר למחבר OBD-J בתא הנהג.\n"
            "• בחר Model ו-Year.\n"
            "• קרא Fault Codes → מחק לאחר תיקון.\n"
            "• בצע Actuator Tests לאימות תיקון.\n\n"
            "רמות חומרה: צהוב = אזהרה. כתום = הגבלת ביצועים (Derate). אדום = כיבוי קרוב — עצור מיידית!"
        ),
        "metadata": {"source": "seed", "topic": "LiveLink,קודי שגיאה,אבחון", "equipment": "JCB 3CX,JCB 4CX,JCB JS300,JCB 540-170", "symptom": "קוד שגיאה,אבחון כללי", "brand": "JCB"}
    },
    {
        "id": "jcb_wheel_loader_427_457_001",
        "text": (
            "תקלות מעמיס גלגלים (Wheel Loader) JCB 427 / 437 / 457\n\n"
            "427 (7.5 טון), 437 (11 טון), 457 (17 טון) — תיבת הילוכים ZF Powershift, הגה ארטיקולציה.\n\n"
            "1. הגה כבד / לא מגיב\n"
            "   גורם: שמן הגה נמוך, Steering Pump שחוקה, Steering Cylinder אטמים פגומים.\n"
            "   בדיקה: לחץ הגה — ערך תקין: 200–220 bar.\n\n"
            "2. Articulation Joint רועש / רפוי\n"
            "   גורם: King Pin / Articulation Pin שחוק.\n"
            "   בדיקה: נסה להזיז הגוף הקדמי — רפיון מעל 3mm = בדוק.\n"
            "   פתרון: החלפת King Pin + Bush.\n\n"
            "3. תיבת הילוכים ZF לא מחליפה\n"
            "   קוד: T-012 — Transmission Neutral Safety.\n"
            "   פתרון: בדוק Neutral Switch, Fuses TCU.\n\n"
            "4. זרוע מטען רועשת בהרמה\n"
            "   גורם: Lift Arm Pin + Bushing שחוקים.\n"
            "   פתרון: שמן Zerck Fittings כל 50 שעות.\n\n"
            "תחזוקה:\n"
            "• שמן ZF Powershift: ZF Lifeguard Fluid 6 — כל 1,000 שעות.\n"
            "• שמן גשר (Axle Oil): SAE 80W-90 — כל 2,000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "הגה,תיבת הילוכים,זרוע", "equipment": "JCB 427,JCB 437,JCB 457", "symptom": "הגה כבד,לא מחליף הילוך", "brand": "JCB"}
    },
    {
        "id": "jcb_compactor_vm115_vm146_001",
        "text": (
            "תקלות קומפקטור/רולר JCB VM115 / VM146\n\n"
            "רולרים כפולים (Tandem Rollers) — VM115 (11.5 טון), VM146 (14.6 טון) — עם מערכת ויברציה הידראולית.\n\n"
            "1. ויברציה לא עובדת\n"
            "   קוד LiveLink: V-001.\n"
            "   גורם: Vibration Solenoid פגום, Vibration Pump לא בונה לחץ.\n"
            "   בדיקה: לחץ ויברציה — ערך תקין: 250–300 bar.\n"
            "   פתרון: בדוק Solenoid → Pump → Vibration Motor.\n\n"
            "2. ויברציה חלשה / תדר נמוך\n"
            "   גורם: שמן הידראולי ויסקוזיות שגויה, Eccentric Weight שחוק.\n"
            "   בדיקה: מד תדר — VM115: 30–33 Hz בתדר גבוה.\n\n"
            "3. גליל (Drum) לא מסתובב\n"
            "   גורם: Drum Drive Motor פגום, Drum Drive Valve תקוע.\n"
            "   בדיקה: לחץ Drum Drive — 300–350 bar.\n\n"
            "4. רולר מסתובב רק לכיוון אחד\n"
            "   גורם: Directional Solenoid Valve פגום.\n\n"
            "5. מים (Water Sprinkler) לא עובד\n"
            "   גורם: Water Pump פגומה, Nozzles סתומות.\n\n"
            "תחזוקה: שמן הידראולי ISO VG 46 — כל 1,000 שעות. בדוק Scraper Blade כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "ויברציה,הידראוליקה,קומפקטור", "equipment": "JCB VM115,JCB VM146", "symptom": "ויברציה לא עובדת,גליל לא מסתובב", "brand": "JCB"}
    },
    {
        "id": "jcb_maintenance_livelink_001",
        "text": (
            "תחזוקה מניעתית JCB — לפי לוח LiveLink\n\n"
            "LiveLink שולח התראות תחזוקה (Service Reminders) לפי שעות מד.\n\n"
            "תחזוקה יומית:\n"
            "• מפלס שמן מנוע (Engine Oil Level) — Dipstick.\n"
            "• מפלס קירור (Coolant Level) — מיכל Coolant.\n"
            "• שמן הידראולי — Sight Glass.\n"
            "• Water Separator — נקה מים.\n"
            "• מסנן אוויר — בדוק אינדיקטור.\n"
            "• שמן Zerck Fittings קריטיים (Bucket, Boom, Stick).\n\n"
            "כל 50 שעות (תחזוקה A):\n"
            "• שמן כל Pivot Pins.\n"
            "• בדוק מתח זחל.\n\n"
            "כל 500 שעות (תחזוקה B):\n"
            "• שמן מנוע JCB 444 + פילטר שמן.\n"
            "• מסנן דלק ראשי (Primary Fuel Filter).\n"
            "• פילטר הידראולי (Return Filter + Pilot Filter).\n"
            "• פילטר Powershift Transmission (3CX/4CX).\n\n"
            "כל 1,000 שעות (תחזוקה C):\n"
            "• שמן תיבת הילוכים (Powershift ATF).\n"
            "• שמן Swing Gear Box (JS Series).\n"
            "• V-Belt + Alternator Belt.\n\n"
            "כל 2,000 שעות (תחזוקה D):\n"
            "• שמן הידראולי מלא (Full Flush).\n"
            "• Final Drive Oil.\n"
            "• Timing Belt — קריטי!"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה,LiveLink,מניעתי", "equipment": "JCB 3CX,JCB 4CX,JCB JS300,JCB 540-170,JCB VM115", "symptom": "תחזוקה מניעתית,לוח שרות", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_backhoe_hoe_001",
        "text": (
            "תקלות זרוע חפירה אחורית (Backhoe) ב-JCB 3CX / 4CX\n\n"
            "הזרוע האחורית מורכבת מבום (Boom), זרוע (Dipper Arm), וכף (Bucket).\n\n"
            "1. Dipper Arm יורד לאחר עצירה (Arm Drift)\n"
            "   גורם: דליפה פנימית בגלינדר ה-Dipper.\n"
            "   בדיקה: הצב זרוע אופקית, כבה מנוע — ירידה מ-10mm ב-5 דקות = החלפת Seals.\n\n"
            "2. Boom לא מגיע לגובה מלא\n"
            "   גורם: שסתום Boom Relief מכוון נמוך.\n"
            "   ערך תקין JCB 3CX: 260–280 bar.\n\n"
            "3. כף חפירה לא נסגרת/נפתחת\n"
            "   גורם: Bucket Cylinder אטמים פגומים, Bucket Pin שחוק.\n"
            "   פתרון: Seal Kit, שמן ו/או החלפת Bucket Pin + Bushing.\n\n"
            "4. Sideshift Boom (JCB 4CX בלבד) זז מעצמו\n"
            "   גורם: Sideshift Cylinder Counterbalance Valve פגום.\n"
            "   פתרון: החלף Counterbalance Valve.\n\n"
            "5. Joystick לא מגיב לתנועה אחת\n"
            "   גורם מכני: כבל פיילוט לשסתום סתום.\n"
            "   גורם חשמלי: Hall Sensor פגום ב-Joystick.\n"
            "   פתרון: בדוק Joystick Sensor ב-ServiceMaster 4."
        ),
        "metadata": {"source": "seed", "topic": "זרוע חפירה,הידראוליקה", "equipment": "JCB 3CX,JCB 4CX", "symptom": "זרוע יורדת,כף לא מגיבה", "brand": "JCB"}
    },
    {
        "id": "jcb_mini_excavator_rubber_track_001",
        "text": (
            "רצועות גומי (Rubber Tracks) ב-JCB 8018 / 8055 / 8085\n\n"
            "מחפרוני מיני JCB (סדרת 8000) משתמשים ברצועות גומי.\n\n"
            "1. רצועה יורדת מהגלגלים (Track De-Rail)\n"
            "   גורם: מתח רצועה נמוך.\n"
            "   בדיקה: מתח נכון JCB 8055: רפיון מרכזי 10–20mm.\n"
            "   כיוון: הוסף גריז ל-Idler Grease Cylinder.\n\n"
            "2. רצועה קרועה / פגומה\n"
            "   גורם: חפצים חדים, גיל מתקדם.\n"
            "   פתרון: החלפת רצועה שלמה — 4–6 שעות ב-8085.\n"
            "   טיפ: בדוק Core Links (קישורי פלדה פנימיים) — שבירה = החלפה דחופה.\n\n"
            "3. רצועה 'קופצת' בנסיעה\n"
            "   גורם: Sprocket שחוק — שיניים מחליקות.\n"
            "   פתרון: החלפת Sprocket ורצועה ביחד.\n\n"
            "4. כלי לא הולך ישר\n"
            "   גורם: מתח שונה בין שתי הרצועות, או Travel Motor לא שווים בלחץ.\n"
            "   פתרון: כיוון מתח רצועה שתי הצדדים שווה.\n\n"
            "טיפים: הימנע מפניות חדות על אספלט. הסר חול שנלכד מתחת לרצועה מדי יום."
        ),
        "metadata": {"source": "seed", "topic": "רצועות גומי,Idler,Sprocket", "equipment": "JCB 8018,JCB 8055,JCB 8085", "symptom": "רצועה יורדת,רצועה קרועה", "brand": "JCB"}
    },
    # ── Old-wave agent: 15 entries ──────────────────────────────────────────
    {
        "id": "jcb_3cx_transmission_001",
        "text": (
            "תקלת שידור (Transmission Fault) ב-JCB 3CX — מכונה לא מתקדמת\n\n"
            "סימפטומים:\n"
            "- מכונה מסרבת לנוע למרות שהמנוע פועל תקין\n"
            "- נסיעה רק בהילוך אחד (Forward בלבד)\n"
            "- קוד שגיאה: E0910 (חיישן מהירות שידור) או E0920 (לחץ הידראולי נמוך בשידור)\n"
            "- שמן שידור עם ריח שרוף או גוון כהה\n\n"
            "סיבות אפשריות:\n"
            "1. מפלס שמן שידור נמוך — הסיבה הנפוצה ביותר.\n"
            "2. מסנן שמן שידור סתום (Transmission Oil Filter) — החלף כל 500 שעות.\n"
            "3. חיישן מהירות (Speed Sensor) בקופסת השידור תקוע.\n"
            "4. בלאי לחצנים (Clutch Packs) פנימיים.\n"
            "5. בקר אלקטרוני (TCU — Transmission Control Unit) פגום.\n\n"
            "שלבי אבחון:\n"
            "שלב 1: בדוק מפלס שמן שידור — Dipstick, בדוק על קרקע ישרה עם מנוע פועל.\n"
            "שלב 2: חבר JCB ServiceMaster 4 ובדוק קודי שגיאה פעילים ב-TCU.\n"
            "שלב 3: מדוד לחץ שמן שידור — לחץ תקין: 14–17 בר (200–250 PSI).\n"
            "שלב 4: בדוק חיישן מהירות — מד-אוהם: 200–1000 אוהם, ללא קצר.\n\n"
            "אזהרות: אל תפעיל ללא שמן תקין — נזק בלתי-הפיך לשידור."
        ),
        "metadata": {"source": "seed", "topic": "שידור", "equipment": "JCB 3CX,JCB 4CX", "symptom": "מכונה לא מתקדמת,שידור", "brand": "JCB"}
    },
    {
        "id": "jcb_js300_swing_003",
        "text": (
            "תקלת מנוע סיבוב (Swing Motor Fault) ב-JCB JS300/JS370\n\n"
            "סימפטומים:\n"
            "- סיבוב איטי לכיוון אחד, רעש טחינה ממנוע הסיבוב\n"
            "- קוד שגיאה: F2250 (לחץ נמוך במעגל סיבוב), F2260 (טמפרטורה גבוהה)\n"
            "- דלף שמן ממנוע הסיבוב לשלדה\n\n"
            "סיבות אפשריות:\n"
            "1. בלאי מנוע הסיבוב (Swing Motor) — דגם JS300: Kawasaki M2X170.\n"
            "2. Counter Balance Valve/Brake Valve של מעגל הסיבוב תקוע.\n"
            "3. בלאי יחידת גלגל פלנטרי (Swing Gearbox Planetary).\n"
            "4. שבירת שן Swing Ring Gear או Pinion.\n"
            "5. Swing Brake לא משתחרר כראוי.\n"
            "6. חוסר סיכה ב-Swing Bearing.\n\n"
            "אבחון:\n"
            "- מדוד לחץ בקווי Swing Motor (A ו-B) — לחץ פיק: 260–280 בר.\n"
            "- בדוק שחרור בלם הסיבוב: לחץ שחרור 35–40 בר.\n"
            "- בדוק מפלס שמן תיבת הסיבוב (EP90).\n\n"
            "תחזוקה: שימון Swing Bearing — כל 10 שעות! Swing Gearbox Oil כל 2,000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "מנוע סיבוב", "equipment": "JCB JS300,JCB JS370", "symptom": "תקלת סיבוב,Swing Motor", "brand": "JCB"}
    },
    {
        "id": "jcb_8055_mini_hydraulic_004",
        "text": (
            "תקלות מחפרון מיני JCB 8055/8085 — לחץ הידראולי נמוך ונסיעה\n\n"
            "סימפטומים ב-JCB 8055:\n"
            "- הזרוע (Boom) לא עולה לגובה המירבי\n"
            "- אחד הזחלים נוסע לאט מהשני\n"
            "- רעש Cavitation בתנועת זרוע מהירה\n"
            "- קוד: 1-2 (תקלת לחץ שמן מנוע), 3-1 (תקלת טמפרטורת קירור)\n\n"
            "סיבות:\n"
            "1. מפלס שמן הידראולי — מכלים קטנים, בדיקה יומית חיונית.\n"
            "2. מסנן הידראולי סתום — החלפה כל 250 שעות (לא 500 כמו במכונות גדולות!).\n"
            "3. בלאי משאבת הידראוליקה הכפולה (Dual Gear Pump): ספיקה גדולה 30 ל\"ד, קטנה 15 ל\"ד.\n"
            "4. Travel Motor (Poclain MS02) — דלף פנימי.\n\n"
            "אבחון:\n"
            "- לחץ מערכת ראשי ב-8055: 205 בר (2975 PSI).\n"
            "- לחץ נסיעה (Travel Circuit): 310 בר (4500 PSI).\n"
            "- בדיקת נסיעה: 10 מטר ישר — חריגה = בעיה ב-Travel Motor.\n\n"
            "תיקון:\n"
            "- מסנן סתום: מק\"ט JCB 32/925682.\n"
            "- Gear Pump שחוקה: JCB 20/925710.\n"
            "- Travel Motor: JCB 20/925420."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,נסיעה", "equipment": "JCB 8055,JCB 8085", "symptom": "לחץ נמוך,נסיעה לקויה", "brand": "JCB"}
    },
    {
        "id": "jcb_457_wheel_loader_hydraulic_005",
        "text": (
            "תקלות מעמיס גלגלים JCB 457/437 — הגה והידראוליקה\n\n"
            "סימפטומים ב-JCB 457:\n"
            "- הגה כבד, מפרק ההגה הארטיקולרי מגיב לאט\n"
            "- קצב הרמת הכף (Bucket) ירד\n"
            "- קוד: E2150 (לחץ הגה נמוך), E2160 (טמפרטורת שמן הגה גבוהה)\n"
            "- דלף שמן ממפרק ההגה המרכזי\n\n"
            "סיבות:\n"
            "1. בלאי אטמים בגלגלי ההגה (Steering Cylinder) — נפוץ לאחר 3,000 שעות.\n"
            "2. בלאי Steering Pump (Bosch-Rexroth ב-JCB 457).\n"
            "3. Priority Valve (שסתום עדיפות להגה) סתום.\n"
            "4. בלאי ציר מפרק ההגה (Articulation Pin/Bushing).\n\n"
            "אבחון:\n"
            "- לחץ מערכת ההגה (TP-Steer): 175–195 בר.\n"
            "- בדוק Priority Valve — פתח ונקה.\n"
            "- בדוק ציר מפרק: נדנוד מעל 5 מ\"מ = בלאי.\n\n"
            "תיקון:\n"
            "- Seal Kit גלגלי הגה: JCB 992/12800.\n"
            "- ציר מפרק: דורש Puller + Press Tooling.\n\n"
            "בטיחות: חסום Safety Bar (כלול בערכת הכלים של JCB 457) לפני עבודה על המפרק!"
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,הגה", "equipment": "JCB 457,JCB 437", "symptom": "הגה כבד,חימום שמן", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_engine_overheating_008",
        "text": (
            "התחממות יתר מנוע (Engine Overheating) ב-JCB 3CX/4CX\n\n"
            "סימפטומים:\n"
            "- מד-טמפרטורה עולה לאזור האדום לאחר 30–60 דקות\n"
            "- אדים מאזור הרדיאטור\n"
            "- קוד: E0310 (טמפרטורת מנוע גבוהה), E0320 (חיישן טמפרטורה פגום)\n"
            "- שמן מנוע בגוון חלבי = מים נכנסו (ראש גלינדרים פגום)\n\n"
            "סיבות אפשריות:\n"
            "1. רדיאטור סתום חיצונית — הסיבה הנפוצה ביותר.\n"
            "2. מפלס נוזל קירור נמוך.\n"
            "3. תרמוסטט (Thermostat) תקוע סגור.\n"
            "4. בלאי משאבת מים (Water Pump Impeller שחוק, דלף מאטם).\n"
            "5. ראש גלינדרים (Head Gasket) פגום.\n"
            "6. Viscous Fan Clutch בלוי.\n\n"
            "אבחון:\n"
            "- בדוק ניקיון רדיאטור — שטוף עם מים בלחץ נמוך מבפנים כלפי חוץ.\n"
            "- בדוק תרמוסטט: אם צינור עליון לא מתחמם = תרמוסטט תקוע.\n"
            "- Block Test Kit: נוזל משנה צבע לירוק = גזי בעירה נכנסו = ראש פגום.\n\n"
            "תיקון: תרמוסטט JCB 02/800483 — שעה. משאבת מים JCB 02/201338 — 2–3 שעות.\n\n"
            "אזהרות: אל תפתח מכסה רדיאטור חם! אל תוסיף מים קרים למנוע חם — סדקים בגוש!"
        ),
        "metadata": {"source": "seed", "topic": "מנוע,קירור", "equipment": "JCB 3CX,JCB 4CX", "symptom": "התחממות יתר מנוע", "brand": "JCB"}
    },
    {
        "id": "jcb_js300_track_010",
        "text": (
            "מערכת הנסיעה (Undercarriage / Track) ב-JCB JS300/JS370\n\n"
            "סימפטומים:\n"
            "- זחל 'יוצא מהמסילה' (Track Derailment) — בפניות חדות\n"
            "- רעש מתכתי מאזור הזחל\n"
            "- קוד: F3100 (תקלת Travel Motor שמאל), F3110 (ימין)\n\n"
            "סיבות:\n"
            "1. מתיחת זחל שגויה — ירידת לחץ ב-Tensioner Cylinder.\n"
            "2. בלאי גלגלי-רגל (Bottom Rollers) וגלגלי-עליון (Carrier Rollers).\n"
            "3. בלאי Sprocket וחוליות השרשרת (Track Link Bushings).\n"
            "4. Travel Motor (Kawasaki MX500) תקוע.\n"
            "5. בלאי אטם ציר (Floating Ring Seal / Duo-Cone Seal) — דלף שמן.\n\n"
            "בדיקת מתיחת זחל:\n"
            "הרחף גלגל אמצעי 10 ס\"מ. מדוד שמיטה (Sag) — תקין: 10–20 מ\"מ. מעל 30 מ\"מ = כיוון.\n\n"
            "תיקון: מלא גריז ל-Tensioner Greaser Cylinder. Sprocket — ניתן להפוך (Reverse).\n"
            "Final Drive Oil: EP90 Gear Oil (1.5–2 ליטר לצד) — כל 2,000 שעות.\n\n"
            "תחזוקה: מתיחת זחל כל 50 שעות. בדיקת גלגלים כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "מערכת זחל,נסיעה", "equipment": "JCB JS300,JCB JS370", "symptom": "זחל יורד,נסיעה", "brand": "JCB"}
    },
    {
        "id": "jcb_paver_htd5_011",
        "text": (
            "תקלות מפסד אספלט (Asphalt Paver) JCB HTD5 / Vibromax\n\n"
            "סימפטומים:\n"
            "- פריסה לא אחידה — פסים ועביות לא שוות\n"
            "- Screed לא מתחמם לטמפרטורה הנדרשת (150–180°C)\n"
            "- קונבייר (Conveyor) עצר\n"
            "- Auger (בורג ספירלה) נסתם — אספלט קפוא\n\n"
            "סיבות:\n"
            "1. חיישן טמפרטורת Screed פגום.\n"
            "2. Screed Heater (גוף חימום) שרוף — עצמאי לכל חצי.\n"
            "3. סתימת Auger — אספלט מצונן.\n"
            "4. Drive Motor לקונבייר — מנוע הידראולי פגום.\n"
            "5. Grade Control Sensor (חיישן שיפוע) כפוף/שגוי.\n\n"
            "אבחון:\n"
            "- בדוק עלייה בטמפרטורת Screed: קצב תקין 5–8°C לדקה.\n"
            "- לחץ קונבייר (TP-Conveyor): 180–220 בר.\n"
            "- מדוד עובי שכבה ב-3 נקודות לרוחב.\n\n"
            "אזהרות: Screed חם 180°C! לבוש כפפות חסינות חום.\n"
            "אסור להניח ידיים ב-Auger בסיבוב — סכנת כריתת אצבעות!"
        ),
        "metadata": {"source": "seed", "topic": "פייבר,אספלט,Screed", "equipment": "JCB HTD5,JCB Vibromax", "symptom": "פריסה לא אחידה,Screed לא מתחמם", "brand": "JCB"}
    },
    {
        "id": "jcb_3cx_dpf_coldstart_012",
        "text": (
            "תקלות הפעלה בקור ו-DPF ב-JCB 3CX Stage IV\n\n"
            "סימפטומים:\n"
            "- קושי בהפעלה מתחת ל-5°C\n"
            "- נורת DPF מהבהבת — מסנן מלא\n"
            "- קוד: E0610 (EGR), E0710 (DPF Regeneration Failed)\n"
            "- ירידת הספק (Engine Derate) עקב DPF מלא\n\n"
            "סיבות לקשיי קור:\n"
            "1. Glow Plugs בלויים — JCB 3CX Stage IV: 4 גלואים.\n"
            "2. מצבר חלש (מתח נמוך מ-12V).\n"
            "3. דלק קיץ בחורף (Waxed Fuel).\n\n"
            "סיבות ל-DPF מלא:\n"
            "1. עבודה ממושכת בסרלנטי (Idling) — DPF לא מגיע ל-600°C לניקוי.\n"
            "2. EGR Valve פגום — פחמן עודף.\n\n"
            "אבחון ל-DPF:\n"
            "- קרא רמת עומס DPF ב-ServiceMaster 4 — מעל 80% = נדרש Regeneration.\n"
            "- בצע Active Regeneration: 20–40 דקות בסרלנטי גבוה.\n"
            "- אם נכשל: Off-Machine Regen במוסך.\n\n"
            "תיקון: גלואים JCB 02/201543 — שעה. Active Regen = מחמם פליטה!\n"
            "אל תבצע Regen במרחב סגור — פליטה מרובה."
        ),
        "metadata": {"source": "seed", "topic": "DPF,הפעלה בקור,מנוע", "equipment": "JCB 3CX Stage IV", "symptom": "קשיי הפעלה בקור,DPF מלא", "brand": "JCB"}
    },
    {
        "id": "jcb_telehandler_540_boom_013",
        "text": (
            "תקלת זרוע טלסקופית ב-JCB 540-170 / 540-200\n\n"
            "סימפטומים:\n"
            "- הזרוע עוצרת ב-60–70% מהאורך המירבי\n"
            "- שמן דולף מתפרי הזרוע בהרחבה מלאה\n"
            "- קוד: T2010 (חיישן אורך זרוע פגום), T2020 (ולוו טלסקופי)\n\n"
            "סיבות:\n"
            "1. בלאי Wear Pads (רפידות שחיקה) — גורם לחיכוך ועצירה.\n"
            "2. חיישן אורך (Boom Length Sensor / Linear Potentiometer) שגוי.\n"
            "3. בלאי אטמי גליל הרחבה (Telescope Cylinder Seals) — דלף פנימי.\n"
            "4. Cylinder Rod כפוף (Bent Telescope Rod) עקב עומס-יתר.\n"
            "5. הגבלת SRS — לא מאפשר הרחבה בזווית הנוכחית עם העומס.\n\n"
            "אבחון:\n"
            "- בדוק Wear Pads: עובי מינימלי 3 מ\"מ.\n"
            "- ServiceMaster: עקוב Boom Length בזמן אמת — ערך 'קופץ' = חיישן פגום.\n\n"
            "תיקון:\n"
            "- Wear Pads: JCB 331/38697. חיישן: JCB 701/80189.\n"
            "- Cylinder Seals: 8–10 שעות עבודה.\n\n"
            "תחזוקה: שמן Wear Pads ב-Molybdenum Grease כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "זרוע טלסקופית", "equipment": "JCB 540-170,JCB 540-200", "symptom": "זרוע לא מתארכת", "brand": "JCB"}
    },
    {
        "id": "jcb_8018_bucket_014",
        "text": (
            "תקלת כף ושסתום עומס ב-JCB 8018/8008 מחפרון מיני\n\n"
            "סימפטומים:\n"
            "- הדלי (Bucket) לא מסתובב לסיגור מלא\n"
            "- הזרוע 'נקפאת' בעמדה אמצעית\n"
            "- שמן הידראולי מתחמם גם בעבודה קלה\n"
            "- Auxiliary (כלים נוספים) לא עובד\n\n"
            "סיבות:\n"
            "1. Overload Relief Valve עבור מעגל ה-Bucket תקוע פתוח.\n"
            "2. בלאי Gear Pump ב-8008 — ספיקה 6–8 ל\"ד בלבד.\n"
            "3. בלוק שסתומים (Control Valve Block) — ב-8008/8018 בלוק אחד לכל מנגנוני השסתומים.\n"
            "4. בלאי גליל ה-Bucket (Bucket Cylinder) — דלף פנימי.\n\n"
            "אבחון:\n"
            "- לחץ ראשי ב-8008: 180–200 בר.\n"
            "- בדוק Overload Relief Valve — נגיש בבלוק הראשי.\n\n"
            "הערות חשובות:\n"
            "- ב-JCB 8008/8018 כל הרכיבים קטנים מאוד — שחיקה זעירה = ירידה גדולה בביצועים.\n"
            "- השתמש בשמן JCB HP32 — לא HP46 כמו במכונות גדולות!"
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,כף", "equipment": "JCB 8008,JCB 8018", "symptom": "כף לא מגיבה,שסתום עומס", "brand": "JCB"}
    },
    {
        "id": "jcb_js300_final_drive_015",
        "text": (
            "תקלת Final Drive (כונן סופי) ב-JCB JS300 — שמן דולף וקול טחינה\n\n"
            "Final Drive = מנגנון גלגל-פלנטרי (Planetary Gearbox) + מנוע נסיעה (Travel Motor) → Sprocket.\n\n"
            "סימפטומים:\n"
            "- שמן דולף מאזור ה-Sprocket\n"
            "- קול טחינה (Grinding) מ-Final Drive בנסיעה\n"
            "- קוד: F3150 (Final Drive שמאל), F3160 (Final Drive ימין)\n"
            "- Final Drive חם מאוד למגע\n\n"
            "סיבות:\n"
            "1. מפלס שמן Final Drive נמוך.\n"
            "2. בלאי מסב פלנטרי (Planetary Bearing).\n"
            "3. שבירת שן גלגל (Gear Tooth Breakage) עקב עומס-יתר.\n"
            "4. בלאי Duo-Cone Seal (Floating Ring Seal) — דלף שמן.\n\n"
            "אבחון:\n"
            "- פתח ברגי מדידה ב-9 ו-3 שעות — שמן צריך לזרום מהפקק ב-9 שעון.\n"
            "- שמן שחור עם שבבי מתכת = בלאי פנימי חמור.\n\n"
            "תיקון:\n"
            "- מלא EP90 Gear Oil (1.5–2 ליטר לצד).\n"
            "- Duo-Cone Seal: תמיד החלף זוג!\n"
            "- Final Drive Assembly: JCB 333/H5832.\n\n"
            "תחזוקה: בדיקת שמן כל 500 שעות. החלפת שמן כל 2,000 שעות.\n"
            "Duo-Cone Seals = אטמים פלדה — ידיים נקיות בלבד, אסור שמן על פני האטם!"
        ),
        "metadata": {"source": "seed", "topic": "כונן סופי,Final Drive", "equipment": "JCB JS300,JCB JS370", "symptom": "דלף שמן Final Drive,קול טחינה", "brand": "JCB"}
    },
    {
        "id": "jcb_telehandler_srs_007",
        "text": (
            "תקלות מערכת SRS ויציבות ב-JCB 535/540 Telehandler\n\n"
            "JCB LiveLink סימפטומים:\n"
            "- מערכת SRS (Stability Reference System) עוצרת הרמה ומאירה אדום\n"
            "- Load Sensing לא עובד — לא מזהה כמה משקל על הכף\n"
            "- הגה ארבע-גלגלים (4WS) לא מתחלף בין מצבים\n"
            "- קוד: T1010 (תקלת SRS), T1020 (חיישן עומס פגום), T1030 (תקלת 4WS)\n\n"
            "סיבות:\n"
            "1. חיישן עומס (Load Moment Indicator / LMI) פגום.\n"
            "2. SRS ECU פגום.\n"
            "3. כיול שגוי — נדרש Calibration מחדש.\n"
            "4. חיישן זווית גלגל (Rear Axle Steering Sensor) לבקרת 4WS.\n\n"
            "אבחון:\n"
            "- בדוק חיישן עומס (LMI): ניוטרל 0.5V, עומס מקסימלי ~4.5V.\n"
            "- SRS Calibration: קרקע שטוחה, זרוע בכלים ריקים.\n"
            "- בדוק ב-ServiceMaster 4: SRS ו-4WS נפרדים.\n\n"
            "בטיחות: לעולם לא לנטרל SRS.\n"
            "בדיקת כיול SRS דורשת מישור מוחלט — שיפוע מעל 2° = כיול שגוי!"
        ),
        "metadata": {"source": "seed", "topic": "SRS,יציבות,Telehandler", "equipment": "JCB 535-95,JCB 540-170", "symptom": "תקלת SRS,עומס יתר", "brand": "JCB"}
    },
]

# Add all entries
added = 0
for entry in JCB_ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} JCB entries. Total KB: {rag.count()} chunks")
