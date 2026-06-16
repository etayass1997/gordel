"""Add Caterpillar (CAT) knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "cat_excavator_hydraulic_001",
        "text": (
            "CAT 320/330/336 - אובדן כוח הידראולי (Loss of Hydraulic Power)\n\n"
            "תסמינים: הזרועות זזות לאט, לחץ נמוך בלוח הבקרה, ירידה בביצועים בחפירה כבדה.\n\n"
            "1. בלאי במשאבות ה-Piston הראשיות (Main Piston Pump Wear)\n"
            "   מחפרוני CAT 320/330/336 מצוידים במשאבות כפולות עם Variable Displacement.\n"
            "   תסמין: לחץ עבודה מתחת ל-330 bar (תקני: 350–380 bar).\n"
            "   בדיקה: חבר מד לחץ (Pressure Gauge) לפורט הבדיקה P1/P2 בגוש השסתומים.\n"
            "   פתרון: אם ספיקה ירדה מעל 15% מהמפרט — החלף משאבה ראשית.\n\n"
            "2. שסתום Relief ראשי פגום (Main Relief Valve)\n"
            "   תסמין: לחץ נמוך באופן אחיד בכל תפקודי הזרוע.\n"
            "   CAT SIS מציין לחץ Relief עבור 320D: 34,300 kPa.\n"
            "   פתרון: נקה את הכדור (Ball) ומושב השסתום (Seat), החלף O-ring, כוון מחדש.\n\n"
            "3. Pump Regulator לא מכוון\n"
            "   הרגולטור שולט ב-Displacement של המשאבה לפי דרישת העומס (Load Sensing).\n"
            "   תסמין: מנוע עמוס בחינם, לחץ מתנדנד.\n"
            "   בדיקה: בדוק קו ה-LS — לחץ צריך להיות 20–25 bar מתחת ללחץ המשאבה.\n\n"
            "4. שמן הידראולי מחומם יתר\n"
            "   מדי הטמפרטורה מציגים אזהרה מעל 95°C.\n"
            "   נקה את מקרר השמן (Oil Cooler) מאבק ולכלוך.\n\n"
            "5. פילטר הידראולי סתום\n"
            "   CAT ממליצה על החלפה כל 500 שעות או כשאינדיקטור הלחץ מוצג.\n"
            "   פילטר סתום גורם לעלייה בלחץ Differential מעל 69 kPa — החלף מיד."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "CAT 320,CAT 330,CAT 336", "symptom": "אובדן כוח הידראולי", "brand": "CAT"}
    },
    {
        "id": "cat_excavator_swing_002",
        "text": (
            "CAT 336 - תקלות מנגנון סיבוב (Swing System Faults)\n\n"
            "תסמינים: סיבוב איטי, קול חריקה מתחת לבית העליון, הכלי לא עוצר בחדות.\n\n"
            "1. שחיקת Swing Bearing (מיסב הסיבוב)\n"
            "   ה-Swing Bearing ב-CAT 336 הוא מיסב עם שיניים פנימיות (Internal Ring Gear).\n"
            "   בדיקה: מדוד את המרווח האנכי (Vertical Clearance) עם שעון מדידה (Dial Indicator).\n"
            "   CAT מגדיר מקסימום 3mm — מעל כן = החלפת Bearing חובה.\n"
            "   שימון: כל 250 שעות עם גריז CAT Bearing Grease 1 (NLGI 1).\n"
            "   נקבי הגריז: 4 נקבים סביב ה-Bearing — שמן עד שגריז זורם החוצה מהאטם.\n\n"
            "2. גיר הסיבוב (Swing Gear Box) — שמן נמוך\n"
            "   CAT 336 נפח שמן גיר סיבוב: כ-4.0 ליטר (SAE 80W-90 GL-4).\n"
            "   תסמין: רעש גריסה חזק בזמן סיבוב, חום מוגבר.\n"
            "   בדיקה: פרק בורג בדיקה (Check Plug) — שמן צריך להגיע לקו.\n\n"
            "3. מנוע הסיבוב ההידראולי (Swing Motor) — בלאי פנימי\n"
            "   לחץ עבודה תקין ב-Swing Motor CAT 336: כ-280–310 bar.\n"
            "   תסמין: מנוע 'טייל' (Drift) לאחר שחרור הג'ויסטיק.\n"
            "   בדיקה: בדוק שסתום ה-Swing Brake — לחץ שחרור: 30–35 bar Pilot.\n"
            "   פתרון: החלף Swing Brake Valve אם לא עוצר תוך 2 שניות.\n\n"
            "4. שיניים שחוקות על Ring Gear\n"
            "   אם שיניים שבורות/שחוקות מעל 30% = החלפת Assembly."
        ),
        "metadata": {"source": "seed", "topic": "מנגנון סיבוב", "equipment": "CAT 336", "symptom": "סיבוב איטי וחריקה", "brand": "CAT"}
    },
    {
        "id": "cat_mini_excavator_301_003",
        "text": (
            "CAT 301 / 303 / 308 מיני מחפרון - תקלות נפוצות\n\n"
            "מיני מחפרוני CAT 301.7/303/308E2 CR מצוידים במנועים קטנים (13–47 כ\"ס) ומערכת הידראוליקה Gear Pump.\n\n"
            "1. זרועות לא מגיבות / לחץ הידראולי אפס\n"
            "   ב-CAT 308E2 CR: משאבה הידראולית מסוג Gear Pump כפולה.\n"
            "   בדיקה ראשונה: רמת שמן הידראולי בצנצנת — ב-301/303 הצנצנת קטנה (כ-12–18 ליטר).\n"
            "   בדיקה שנייה: לחץ Pilot (הפקודות לשסתומים) — צריך 30 bar.\n"
            "   פתרון: בדוק את מתג ה-Safety Lock Lever — אם הנוף אינו ב-UNLOCK, המערכת חסומה.\n\n"
            "2. Blade (להב הדחפור) לא עולה ב-CAT 303/308\n"
            "   תסמין: להב עולה לאט מאוד או לא עולה.\n"
            "   בדיקה: לחץ הידראולי בכניסה לגלינדר Blade צריך להיות 200–250 bar.\n\n"
            "3. מנוע קטן מתחמם מהר (Yanmar Engine Overheat)\n"
            "   CAT 301/303 מצוידים במנועי Yanmar (2TNV70/3TNV74).\n"
            "   מערכת קירור מינימלית — חשוב לנקות רדיאטור כל 100 שעות!\n\n"
            "4. מתח רצועת מיני מחפרון\n"
            "   CAT 301/303 עם רצועות גומי (Rubber Tracks).\n"
            "   מתח תקין: רפיון של 10–15mm במרכז הרצועה בין ה-Idler ל-Sprocket.\n"
            "   מתח נמוך מדי = רצועה נופלת. גבוה מדי = בלאי מהיר של Rollers."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,מנוע", "equipment": "CAT 301,CAT 303,CAT 308", "symptom": "אין תגובה בזרועות", "brand": "CAT"}
    },
    {
        "id": "cat_wheel_loader_950_004",
        "text": (
            "CAT 950GC / 966M טעון גלגלים - בעיות בלמים ותיבת הילוכים\n\n"
            "טוענים CAT 950/966 מצוידים ב-Power Shift Transmission ובלמי Wet Disc (דיסקים בשמן).\n\n"
            "1. בלמים חלשים / לא בולמים (Brake Fade)\n"
            "   CAT 950/966 עם Wet Disc Brakes — הבלמים עובדים בשמן הגיר.\n"
            "   בדיקה: לחץ בלם צריך להיות 110–138 bar בזמן לחיצה מלאה.\n"
            "   גורם נפוץ: Brake Accumulators (מצברי לחץ) ריקים.\n"
            "   בדוק לחץ Pre-charge (חנקן, N₂): 55 bar.\n"
            "   פתרון: אם Accumulator מרוקן — החלף או מלא חנקן לפי מפרט CAT.\n\n"
            "2. החלקת Clutch בתיבת הילוכים (Transmission Clutch Slip)\n"
            "   תסמין: הכלי 'גולש' בהעמסה כבדה, הילוך ראשון לא מחזיק עלייה.\n"
            "   שמן תקני: CAT TO-4 בלבד! שמן אחר = נזק לדיסקים בתוך 100 שעות.\n"
            "   בדיקה CAT ET: בדוק לחץ Clutch בכל הילוך.\n"
            "   פתרון: נקז ומלא שמן Transmission (CAT TO-4), בדוק פילטר.\n\n"
            "3. רעש גיר / Torque Converter בעיה\n"
            "   תסמין: רעש שריקה מתא הגיר בהאצה, מהירות מוגבלת.\n"
            "   בדיקה: טמפרטורת שמן Torque Converter — מעל 120°C = בעיה.\n"
            "   פתרון: בדוק שסתום ה-Transmission Modulating Valve.\n\n"
            "4. Axle Oil — שמן גחון\n"
            "   CAT 950/966 עם Tandem Axle — שמן Final Drive נפרד מהגיר.\n"
            "   החלף שמן Final Drive כל 2000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "בלמים,הנעה", "equipment": "CAT 950,CAT 966", "symptom": "בלמים חלשים ורעש גיר", "brand": "CAT"}
    },
    {
        "id": "cat_wheel_loader_966_hydraulic_005",
        "text": (
            "CAT 966M/966H - כשל בעליית הזרוע בעומס (Lift Arm Failure Under Load)\n\n"
            "תסמין מרכזי: הזרוע עולה תקין בלי עומס, אבל 'מתקשה' או נעצרת בעומס מלא.\n\n"
            "1. לחץ Relief הזרוע נמוך (Boom Lift Relief Valve)\n"
            "   CAT 966M: לחץ Relief לעליית הזרוע: 34,500 kPa (345 bar).\n"
            "   בדיקה: חבר מד לחץ לפורט בגוש השסתומים.\n"
            "   פתרון: כוון את שסתום ה-Relief של זרוע ההרמה לערך מפרטי.\n\n"
            "2. משאבה ראשית — ירידת ספיקה\n"
            "   CAT 966 עם משאבת Piston משתנה (Variable Displacement Piston Pump).\n"
            "   בדיקה: Flow Test דרך CAT ET — בדוק Actual vs. Commanded Displacement.\n\n"
            "3. Pilot Operated Check Valve סתום\n"
            "   ניקוי: פרק שסתום, נקה כדור (Ball) ומושב, בדוק O-rings.\n\n"
            "4. גלינדר זרוע — אטם פנימי בלוי (Lift Cylinder Internal Seal)\n"
            "   תסמין: הזרוע יורדת לאט תוך 10 דקות כאשר המנוע כבוי.\n"
            "   בדיקה: הרם לגובה מקסימום, כבה מנוע, המתן 10 דקות — ירידה מעל 50mm = דליפה פנימית.\n"
            "   פתרון: החלף ערכת אטמים (Seal Kit) לגלינדר ה-Boom.\n\n"
            "5. Bucket Positioner / Return-to-Dig בעיה\n"
            "   CAT 966 עם Return-to-Dig אוטומטי — אם הכף לא חוזרת לזווית חפירה = בדוק חיישן זווית."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "CAT 966", "symptom": "זרוע לא עולה בעומס", "brand": "CAT"}
    },
    {
        "id": "cat_paver_ap1055_006",
        "text": (
            "CAT AP1055 מרצף אספלט - תקלות מערכת הפיזור (Screed System)\n\n"
            "ה-CAT AP1055 הוא מרצף עם Screed נמתחת (Extending Screed) ומערכת חימום חשמלית/גז.\n\n"
            "1. עובי שטיח לא אחיד (Mat Thickness Inconsistency)\n"
            "   גורמים:\n"
            "   א. Tow Point Cylinders לא מסונכרנים — בדוק לחץ בשני הצדדים (צריך זהה ±5 bar).\n"
            "   ב. Screed Attack Angle (זווית התקפה) לא נכון — כוון לפי הוראות CAT.\n"
            "   ג. רמת Auger לא שווה — חומר צריך להיות ב-2/3 גובה לוח Auger.\n\n"
            "2. Screed לא מתחממת (Screed Not Heating)\n"
            "   CAT AP1055 עם Electric Heating Elements.\n"
            "   בדיקה: מדוד התנגדות של כל Element — חוט שרוף = אינסוף אוהם.\n"
            "   ערך תקין: ~8–15 אוהם.\n"
            "   פתרון: החלף Heating Element הפגום, בדוק חיבורי חשמל ל-Screed.\n\n"
            "3. Auger לא מסתובב\n"
            "   גורם א: מנוע הידראולי של Auger פגום.\n"
            "   גורם ב: שסתום ה-Auger תקוע סגור.\n"
            "   בדיקה: לחץ הידראולי ל-Auger Motor — צריך 200–250 bar בעומס.\n\n"
            "4. Conveyor (מסועי הזנה) לא מזין\n"
            "   בדיקה: בדוק חיישן גובה חומר (Material Level Sensor/Paddle Sensor) — ייתכן תקוע.\n"
            "   פתרון: נקה חיישן מגע, בדוק מנוע הידראולי של Conveyor."
        ),
        "metadata": {"source": "seed", "topic": "אספלט,מערכת הפיזור", "equipment": "CAT AP1055", "symptom": "רוחב שטיח לא אחיד", "brand": "CAT"}
    },
    {
        "id": "cat_compactor_cs74_007",
        "text": (
            "CAT CS74 / CP74 מדחס - תקלות מערכת הרטט (Vibratory System)\n\n"
            "CAT CS74 הוא מדחס עם תוף חלק (Smooth Drum), CP74 עם תוף פד (Padded Drum).\n"
            "תדר רטט: 28–33 Hz, עוצמת G: ~390 kN.\n\n"
            "1. ויברציה לא פועלת (No Vibration)\n"
            "   גורמים:\n"
            "   א. מנוע ויברציה הידראולי (Vibration Motor) פגום — בדוק לחץ: צריך ~300–350 bar.\n"
            "   ב. שסתום בקרת ויברציה (Vibration Control Valve) תקוע סגור.\n"
            "   ג. Exciter Weight (משקולת אקסנטרית) שבורה — פרק Drum ובדוק.\n"
            "   בדיקה CAT ET: קוד שגיאה E2100 ומעלה = בעיית מערכת הרטט.\n\n"
            "2. ויברציה לא מספקת (Low Amplitude)\n"
            "   גורם: Eccentric Shaft Bearings בלויים.\n"
            "   פתרון: פרק Drum, בדוק ושמן מיסבי הציר.\n\n"
            "3. Drum Drive לא מסתובב (No Drum Propulsion)\n"
            "   CAT CS74 עם Drum Motor נפרד להנעת התוף.\n"
            "   בדיקה: Hydrostatic Drive System — בדוק לחץ Charge (25–30 bar) בלולאת ה-Closed Loop.\n"
            "   גורם: Charge Pump פגום = אין הנעה.\n\n"
            "4. רוחב הדחסה לא אחיד\n"
            "   CAT CP74: פדים (Pads) שחוקים לא שווה.\n"
            "   בדוק כל Pad לשחיקה — עיין מפרט עובי מינימלי בהוראות CAT.\n\n"
            "5. מערכת קירור Drum (Drum Water System)\n"
            "   בעבודה באספלט — חשוב להפעיל מערכת רטבת ה-Drum.\n"
            "   בדוק ראשי התזה (Spray Nozzles) לסתימות — סתום = אספלט נדבק לתוף."
        ),
        "metadata": {"source": "seed", "topic": "רטט,הנעה", "equipment": "CAT CS74,CAT CP74", "symptom": "ויברציה לא עובדת", "brand": "CAT"}
    },
    {
        "id": "cat_skid_steer_226d_008",
        "text": (
            "CAT 226D / 242D / 272D עגלת פינוי (Skid Steer) - תקלות היגוי והנעה\n\n"
            "Skid Steer מתנהג בהיגוי דיפרנציאלי — כל צד נע במהירות נפרדת.\n\n"
            "1. הכלי לא פונה / פונה לצד אחד בלבד\n"
            "   גורם א: תקלת Hydrostatic Drive באחד הצדדים.\n"
            "   CAT 226D/242D עם מנועי Piston Hydrostatic — בדוק כל מנוע בנפרד.\n"
            "   בדיקה: לחץ בלולאת ה-Drive (High Pressure Loop) צריך ~410 bar בעומס.\n"
            "   גורם ב: Joystick Controller (EH Control) — בעיית חיישן.\n"
            "   בדיקה: CAT ET — בדוק Joystick Position Sensor Values.\n\n"
            "2. מהירות שונה בין ימין לשמאל\n"
            "   CAT 272D עם Two-Speed Drive — בדוק מתג High/Low Speed.\n"
            "   גורם: Charge Pressure נמוך באחד מהמנועים.\n"
            "   בדיקה: לחץ Charge — צריך 25–35 bar.\n"
            "   פתרון: בדוק סנן Charge (Charge Filter) — סתום = לחץ Charge נופל.\n\n"
            "3. Parking Brake לא משתחרר\n"
            "   CAT Skid Steer — Parking Brake ספרינגי, נשחרר בלחץ הידראולי Pilot.\n"
            "   בדיקה: לחץ Pilot (Brake Release) — צריך 24–30 bar לשחרור.\n"
            "   פתרון: החלף Charge Pump אם לחץ Charge נמוך מ-20 bar.\n\n"
            "4. Lift Arm לא עולה\n"
            "   CAT 272D — לחץ עבודה לזרוע: ~250 bar. בדיקה: שסתום ה-Relief לזרוע.\n\n"
            "5. Auxiliary Hydraulics לא עובד\n"
            "   CAT 272D עם High Flow Auxiliary (90+ l/min).\n"
            "   גורם: High Flow Solenoid Valve פגום.\n"
            "   בדיקה: CAT ET — בדוק פקודות ל-Auxiliary Solenoid, מדוד 12–24V על הסולנואיד."
        ),
        "metadata": {"source": "seed", "topic": "הנעה,היגוי", "equipment": "CAT 226D,CAT 242D,CAT 272D", "symptom": "כלי לא פונה,מהירות שונה בין הצדדים", "brand": "CAT"}
    },
    {
        "id": "cat_excavator_engine_320_009",
        "text": (
            "CAT 320D2/330D2 - תקלות מערכת Tier 4 / DEF (AdBlue)\n\n"
            "CAT 320D2 ו-330D2 עם מנוע C7.1/C9.3 עם מערכת Aftertreatment (SCR + DPF).\n\n"
            "1. אזהרת DEF נמוכה — Inducement (תגבול הדרגתי)\n"
            "   CAT 320D2: כאשר DEF נמוך מ-10% — מופיע אזהרה בלוח.\n"
            "   כאשר ריק — מנוע מוגבל ל-25% כוח (Inducement Derate).\n"
            "   פתרון מיידי: מלא DEF (ISO 22241, 32.5% אוריאה) לפי קו MAX.\n"
            "   שימו לב: אין להשתמש במים רגילים! נזק מיידי ל-DEF Injector.\n\n"
            "2. DEF Injector סתום / פגום\n"
            "   תסמין: קוד שגיאה CA3714 (DEF Injection Fault) ב-CAT ET.\n"
            "   גורם: DEF התגבש (Crystallization) בזמן חוסר שימוש.\n"
            "   פתרון: הפעל Purge Cycle דרך CAT ET (מנקה את ה-Injector אוטומטית).\n"
            "   אם לא עוזר: פרק Injector, נקה במים חמים בלבד.\n\n"
            "3. DPF מלא — Regeneration נדרש\n"
            "   תסמין: נורת DPF דולקת, קוד CA3702, ביצועים מוגבלים.\n"
            "   פתרון: בצע Stationary Regeneration ידנית דרך CAT ET.\n"
            "   אזהרה: אל תבצע Regen ליד חומרים דליקים! טמפרטורת פלטה עולה מעל 600°C.\n\n"
            "4. DEF Quality Fault\n"
            "   קוד CA3713 — DEF מזוהם, מהול מדי, או ריכוז אוריאה שגוי.\n"
            "   בדוק: ריכוז אוריאה עם Refractometer — צריך להיות 32.5% ±1.5%.\n"
            "   פתרון: נקז מיכל DEF לחלוטין, שטוף במים מזוקקים, מלא DEF חדש ומאושר."
        ),
        "metadata": {"source": "seed", "topic": "מנוע,DEF,AdBlue", "equipment": "CAT 320,CAT 330", "symptom": "קוד שגיאה DEF ומנוע מוגבל", "brand": "CAT"}
    },
    {
        "id": "cat_excavator_track_336_010",
        "text": (
            "CAT 336 - תקלות מערכת הנסיעה (Travel System) וזחלים\n\n"
            "1. הכלי לא נוסע לכיוון אחד (One-Sided Travel Fault)\n"
            "   CAT 336 עם שני Travel Motors נפרדים.\n"
            "   בדיקה: חבר מד לחץ ל-Test Ports של כל Travel Motor (A/B Ports).\n"
            "   לחץ תקין: ~420 bar בעומס מלא.\n"
            "   פתרון: בדוק Anti-Cavitation Valve ו-Counterbalance Valve.\n\n"
            "2. Counterbalance Valve (שסתום נגד גרביטציה) פגום\n"
            "   תסמין: הכלי 'מתגלגל' בהורדת מדרון ללא שליטה.\n"
            "   פתרון: החלף Counterbalance Valve Assembly.\n\n"
            "3. שחיקת Sprocket מואצת\n"
            "   CAT 336 Sprocket: בלאי תקין מעל 5000 שעות.\n"
            "   תסמין: שיניים 'דקות' יותר מ-50% מעובי מקורי.\n"
            "   פתרון: החלף Sprocket + Chains ביחד (לא אחד בלי השני!).\n\n"
            "4. Track Shoe Bolts מתפשטים\n"
            "   CAT 336: הידוק בורגי נעלי זחל — 475 Nm (350 ft-lbs).\n"
            "   בדוק כל 250 שעות.\n\n"
            "5. Final Drive Oil Seal דולף\n"
            "   תסמין: שמן כהה על הזחל מאחורי Sprocket.\n"
            "   CAT 336 Final Drive: 7.5 ליטר SAE 80W-90.\n"
            "   פתרון: החלף Float Seal — עבודה של ~8 שעות.\n"
            "   אין לדחות! דליפה ממושכת = נזק ל-Carrier Roller Bearings."
        ),
        "metadata": {"source": "seed", "topic": "זחלים,הנעה", "equipment": "CAT 336", "symptom": "נסיעה חד צדדית ובלאי זחל", "brand": "CAT"}
    },
    {
        "id": "cat_wheel_loader_950_engine_011",
        "text": (
            "CAT 950GC / 966M - חוסר כוח מנוע ועשן שחור (Power Loss & Black Smoke)\n\n"
            "מנועי C7.1 (950GC) ו-C9.3 (966M) עם Turbocharger ומערכת Common Rail Injection.\n\n"
            "1. עשן שחור בעבודה כבדה (Black Smoke Under Load)\n"
            "   גורם א: מסנן אוויר (Air Filter) סתום — אינדיקטור מסנן אוויר בלוח: אם דולק, החלף מיד.\n"
            "   גורם ב: Turbocharger לא בונה לחץ.\n"
            "   בדיקה: Boost Pressure צריך להיות ~170–210 kPa עבור C7.1 בעומס.\n"
            "   גורם ג: Fuel Injector פגום — מזריק יתר דלק.\n"
            "   אבחון CAT ET: בדוק Balance Rates — חריגה מ-±4 mg/st = החלף.\n\n"
            "2. חוסר כוח בעלייה (Lack of Power on Grade)\n"
            "   גורם א: EGR Valve (שסתום החזרת גזים) סתום פתוח.\n"
            "   בדיקה CAT ET: בדוק EGR Position Sensor, ניקוי EGR Valve בספריי מנקה.\n"
            "   גורם ב: VGT Turbocharger תקוע.\n"
            "   פתרון: CAT ET → Active Tests → בצע VGT Calibration.\n\n"
            "3. Aftercooler סתום (ATAAC)\n"
            "   תסמין: Intake Manifold Temperature גבוה מ-70°C.\n"
            "   פתרון: נקה Aftercooler Fins בלחץ אוויר (מהפנים החוצה).\n\n"
            "4. DPF Soot Level גבוה\n"
            "   CAT 950GC: אם DPF Soot Level מעל 100% (CAT ET) = Forced Regeneration."
        ),
        "metadata": {"source": "seed", "topic": "מנוע,כוח,DEF", "equipment": "CAT 950,CAT 966", "symptom": "חוסר כוח בעלייה ועשן שחור", "brand": "CAT"}
    },
    {
        "id": "cat_skid_steer_272d_hydraulic_012",
        "text": (
            "CAT 272D / 242D - תקלות מערכת Auxiliary Hydraulics לאביזרים\n\n"
            "CAT 272D עם High Flow Option (90 l/min) ו-Standard Flow (55 l/min).\n"
            "מיועד להפעלת פטישים (Hydraulic Breaker), מברגות (Auger), מלחציים (Grapple) ועוד.\n\n"
            "1. אביזר Hydraulic Breaker לא פועל\n"
            "   גורם א: מתג High Flow לא הופעל — בלוח CAT 272D יש לחצן 'High Flow'.\n"
            "   גורם ב: Auxiliary Control Valve (AUX Valve) פגום.\n"
            "   בדיקה: מדוד לחץ בחיבורי AUX (Flat-Face Couplers) — צריך ~250 bar בעומס.\n\n"
            "2. זרימה חלשה ל-Auger\n"
            "   גורם: GPM Setting לא מכוון נכון לאביזר.\n"
            "   CAT 272D: כוון ספיקת Auxiliary דרך CAT ET → Machine Parameters → AUX Flow.\n"
            "   ערך מומלץ: Auger = 50–70 l/min, Breaker = 80–90 l/min.\n\n"
            "3. Auxiliary חם מדי (Aux Hydraulics Overheating)\n"
            "   פתרון: בדוק ש-Back Pressure מה-Breaker (Return Line) אינו מעל 15 bar.\n\n"
            "4. Coupler לא מתנתק (Stuck Coupler)\n"
            "   גורם: לחץ שארית (Residual Pressure) בקווי AUX.\n"
            "   פתרון: לפני ניתוק — הפעל AUX לשנייה (לפרוק לחץ), ואז נתק Coupler.\n"
            "   שמן את O-rings של Couplers בגריז קל כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,אביזרים", "equipment": "CAT 272D,CAT 242D", "symptom": "אביזר הידראולי לא עובד,זרימה חלשה", "brand": "CAT"}
    },
    {
        "id": "cat_excavator_boom_arm_330_013",
        "text": (
            "CAT 330 - דליפות גלינדרים וצניחת זרועות (Cylinder Drift & External Leaks)\n\n"
            "1. Boom (זרוע ראשית) צונחת לאחר כיבוי מנוע\n"
            "   תסמין: הנח זרוע בגובה מקסימום, כבה מנוע — זרוע יורדת מעל 100mm תוך 10 דקות.\n"
            "   גורם א: Load Check Valve (שסתום בדיקת עומס) פגום בגוש השסתומים.\n"
            "   פתרון: פרק גוש שסתומים, נקה/החלף Load Check Valve Ball + Spring.\n"
            "   גורם ב: אטמי גלינדר Boom (Cylinder Internal Seals) בלויים.\n"
            "   פתרון: Seal Kit לגלינדר Boom CAT 330 — כ-4–6 שעות עבודה.\n\n"
            "2. דליפת שמן חיצונית מגלינדר (External Cylinder Leak)\n"
            "   תסמין: שמן על גבעול הגלינדר (Rod), מחמיר בקור.\n"
            "   גורם: Wiper Seal ו-Rod Seal בלויים.\n"
            "   פתרון: פרק גלינדר, החלף Seal Kit מלא (Wiper + Rod + Piston Seals).\n\n"
            "3. Stick (זרוע שנייה) נופלת מהר\n"
            "   בדיקה: הגדר Stick ב-90° אופקי, כבה — אם נופל תוך 2 דקות = בעיה.\n"
            "   פתרון: נקה/החלף Load Check Valve ב-Stick Circuit.\n\n"
            "4. Bucket (כף) נע לבד\n"
            "   גורם: Regeneration Valve תקוע פתוח = לחץ לא שווה.\n"
            "   פתרון: בדוק Bucket Regeneration Circuit בגוש השסתומים.\n\n"
            "5. דליפת O-ring בחיבורי צינורות הידראוליים\n"
            "   O-rings נפוצים בגלינדרי CAT 330: BOSS O-ring (מסוג SAE 6000).\n"
            "   שמן O-ring חדש בשמן הידראולי לפני הידוק."
        ),
        "metadata": {"source": "seed", "topic": "זרועות,גלינדרים", "equipment": "CAT 330", "symptom": "זרוע צונחת ודליפת שמן גלינדר", "brand": "CAT"}
    },
    {
        "id": "cat_compactor_cs74_engine_014",
        "text": (
            "CAT CS74 / CP74 מדחס - כיבוי מנוע בעבודה ורעידות חריגות\n\n"
            "CAT CS74 מצוייד במנוע C3.3B (74 כ\"ס, Tier 4 Final), מערכת רטט הידראולית.\n\n"
            "1. מנוע נכבה פתאום בעבודה (Engine Stall Under Load)\n"
            "   גורם א: מסנן דלק סתום — שני מסנני דלק: Primary ו-Secondary.\n"
            "   גורם ב: מים בדלק (Water in Fuel) — Water Separator מלא.\n"
            "   בדיקה: בדוק Water Separator ב-Primary Filter — נקה מים מדי שבוע.\n"
            "   גורם ג: Hydraulic Load גבוה מדי = מנוע 'חנוק'.\n\n"
            "2. רעידות חריגות בהנעה (Abnormal Body Vibration)\n"
            "   גורם א: Drum Drive Coupling שחוק.\n"
            "   גורם ב: Engine Mounts בלויים (ריפודי מנוע) — פרק, בדוק, החלף אם נסדקו.\n"
            "   גורם ג: Eccentric Shaft Imbalance — אם שבר Eccentric Weight.\n"
            "   תסמין: רעידה חריגה חדשה שהחלה פתאום.\n\n"
            "3. מנוע לא עולה בבוקר קר (Cold Start Issues)\n"
            "   CAT C3.3B עם Glow Plugs (נרות להט).\n"
            "   מדידה: אמפר-מטר על חוט ל-Glow Plug — צריך 15–20A לנר.\n"
            "   פתרון: החלף נרות להט שלא מחמם.\n\n"
            "4. עצירת חירום (Emergency Stop) אוטומטית\n"
            "   CAT CS74 הגנות אוטומטיות עוצרות מנוע:\n"
            "   - לחץ שמן מנוע נמוך (< 70 kPa)\n"
            "   - טמפרטורת מנוע גבוהה (> 107°C)\n"
            "   - רמת DEF נמוכה (< 5%)\n"
            "   בדיקה: חבר CAT ET, בדוק Event Codes — הקוד יגיד מה הפעיל העצירה."
        ),
        "metadata": {"source": "seed", "topic": "מנוע,עצירות", "equipment": "CAT CS74,CAT CP74", "symptom": "מנוע נכבה בעבודה ורעידות חריגות", "brand": "CAT"}
    },
    {
        "id": "cat_excavator_cab_electrical_015",
        "text": (
            "CAT 320/330/336 - תקלות לוח בקרה, CAN Bus וחשמל תא נהג\n\n"
            "1. מסך מוניטור CAT לא דולק\n"
            "   גורם א: נתיך (Fuse) מסך שרוף.\n"
            "   CAT 320D2 - קופסת נתיכים: בתא נהג, מכסה תחתון ימין.\n"
            "   גורם ב: חיבור מחבר (Harness Connector) למסך רופף.\n"
            "   פתרון: בדוק Deutsch Connector מאחורי המסך — נקה ושדך מחדש.\n\n"
            "2. קודי שגיאה CAN Bus מרובים\n"
            "   גורם: תקלת רשת CAN Bus בין ECM (Engine Control Module) ל-MCM (Machine Control Module).\n"
            "   אבחון: CAT ET → Communications → בדוק אילו מודולים 'Online'.\n"
            "   בדיקת עמידות CAN Bus בין CAN+ ל-CAN- — צריך 60 אוהם.\n\n"
            "3. Joystick EH (Electrohydraulic) לא מגיב\n"
            "   CAT 320D2/330D2 עם Joystick חשמלי — אותות אנלוגיים ל-MCM.\n"
            "   בדיקה CAT ET: Machine Systems → Joystick → בדוק Signal Voltage (0.5–4.5V בתנועה).\n"
            "   פתרון: החלף Joystick Assembly.\n\n"
            "4. מצלמה אחורית (Rear View Camera) לא עובדת\n"
            "   גורם: כבל וידאו (Coax Cable) קצר בסיבוב התא.\n"
            "   פתרון: בדוק כבל מהמצלמה ל-Monitor, כולל נקודת המעבר ב-Swing Bearing Ring.\n\n"
            "5. Alternator לא טוען (Charging System Fault)\n"
            "   בדוק מתח סוללה: במנוע דולק — צריך 27.5–28.5V (מערכת 24V).\n"
            "   CAT 330D2: Alternator 24V 80A.\n"
            "   גורם נפוץ: רצועת Alternator (Serpentine Belt) החליקה."
        ),
        "metadata": {"source": "seed", "topic": "חשמל,תא נהג,CAN Bus", "equipment": "CAT 320,CAT 330,CAT 336", "symptom": "תצוגת לוח לא עובדת וקודי שגיאה מרובים", "brand": "CAT"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} CAT entries. Total KB: {rag.count()} chunks")
