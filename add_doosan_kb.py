"""Add Doosan/Develon and Bobcat knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "doosan_excavator_hydraulic_001",
        "text": (
            "תקלות מערכת הידראוליקה במחפרוני דוסאן/דוולון DX300 / DX340 / DX380\n\n"
            "דגמים: DX300LC-7, DX340LC-7, DX380LC-7 (מנועי D-Series)\n\n"
            "מערכת ההידראוליקה מורכבת ממשאבה כפולה (Tandem Piston Pump), בלוק שסתומים ראשי (Main Control Valve), "
            "מנועי נסיעה (Travel Motors), מנועי סיבוב (Swing Motor) וגלינדרים (Boom/Stick/Bucket Cylinders).\n\n"
            "1. אובדן כוח כללי בכל תנועות ה-Boom/Stick/Bucket\n"
            "   סיבה: לחץ הידראולי ראשי (Main Relief Pressure) ירד. ב-DX300 הלחץ הנומינלי הוא 350 bar.\n"
            "   בדיקה: חבר מד לחץ לנקודת בדיקה P1/P2 בגוף המשאבה. אם לחץ מתחת ל-300 bar = בעיה.\n"
            "   פתרון: כוונן Main Relief Valve. אם לא מגיע ללחץ לאחר כוונון = החלף שסתום.\n\n"
            "2. Boom יורד לבד (Boom Drift)\n"
            "   סיבה: Boom Hold Valve (Anti-Drift Valve) דולף.\n"
            "   בדיקה: הרם Boom לגובה מקסימלי, כבה מנוע. מדד ירידה לאחר 5 דקות. יותר מ-10mm = בעיה.\n"
            "   פתרון: פרק ונקה את ה-Boom Hold Valve, בדוק O-rings, החלף אם נדרש.\n\n"
            "3. תגובה איטית של הג'ויסטיקים\n"
            "   סיבה: לחץ Pilot נמוך (Pilot Pressure). ב-DX300 הלחץ הנדרש: 38 bar.\n"
            "   בדיקה: חבר מד לחץ לנקודת Pilot Port על גבי בלוק הג'ויסטיקים.\n"
            "   פתרון: בדוק משאבת Pilot (Pilot Pump), בדוק פילטר Pilot (לרוב 10 מיקרון), החלף אם סתום.\n\n"
            "4. שמן הידראולי חם מדי (Overheating) — אזעקה מעל 95°C\n"
            "   נקה את ה-Oil Cooler מאבק ולכלוך (לחץ אוויר נגד כיוון זרימה).\n"
            "   בדוק מאוורר (Fan Motor) ותרמוסטט שמן (Oil Thermostat Valve).\n\n"
            "5. רעש גבוה מהמשאבה — Cavitation\n"
            "   בדיקה: בדוק כל חיבורי היניקה לשמן. בדוק O-rings בתקע כניסת השמן.\n"
            "   פתרון: הדק חיבורים, החלף O-rings. אם הרעש נמשך = בדוק מסנן שאיבה (Suction Strainer)."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "DX300,DX340,DX380", "symptom": "בעיות לחץ הידראולי", "brand": "Doosan"}
    },
    {
        "id": "doosan_net_diagnostics_001",
        "text": (
            "אבחון עם מערכת DOOSAN-Net / Hi-MATE במחפרוני דוסאן ודוולון\n\n"
            "DOOSAN-Net (Hi-MATE Remote Management) מאפשר ניטור מרחוק ואבחון מקצועי.\n\n"
            "גישה לקודי שגיאה דרך לוח המכשירים:\n"
            "1. כבה את הכלי לחלוטין.\n"
            "2. החזק את כפתור ה-MODE על גבי לוח הבקרה.\n"
            "3. הפעל גורם הנעה (Key On) תוך כדי החזקת כפתור.\n"
            "4. קודי שגיאה פעילים יוצגו בפורמט E + מספר (למשל E0302).\n\n"
            "קודי שגיאה נפוצים:\n"
            "E0302 — תקלת חיישן טמפרטורת שמן הידראולי (Hydraulic Oil Temp Sensor)\n"
            "   פתרון: החלף חיישן טמפרטורה שמן הידראולי (NTC Sensor). מיקום: על גבי ה-Hydraulic Tank.\n\n"
            "E0410 — תקלת חיישן לחץ Pilot (Pilot Pressure Sensor Fault)\n"
            "   פתרון: בדוק חיישן לחץ Pilot, בדוק חיבורי חשמל לחיישן.\n\n"
            "E0601 — תקלת תקשורת CAN Bus בין ECM למסוף (ECM-Monitor CAN Fault)\n"
            "   תסמין: מסך לוח שחור, קודי שגיאה מרובים בו זמנית.\n"
            "   פתרון: בדוק כבל CAN (שני חוטים: CAN Hi / CAN Lo), בדוק מסיים CAN (120 אוהם בין קצוות).\n\n"
            "E0204 — תקלת מנוע: לחץ שמן נמוך (Engine Oil Pressure Low) — עצור מנוע מיד!\n"
            "   בדוק מפלס שמן מנוע. בדוק חיישן לחץ שמן. בדוק משאבת שמן מנוע.\n\n"
            "E0901 — אזעקת מסנן הידראולי (Hydraulic Filter Clogged)\n"
            "   פתרון: החלף מסנן הידראולי (Return Filter). ב-DX300 = Doosan חלק 400404-00241.\n\n"
            "חיבור DOOSAN-Net Scanner:\n"
            "   יציאת OBD: ממוקמת בתא המפעיל, מתחת ללוח שמאל.\n"
            "   תוכנה: Doosan Diagnostic Tool (DDT) או Hi-MATE Diagnostics.\n"
            "   פרוטוקול: CAN-ISO 11898 ב-250 kbps."
        ),
        "metadata": {"source": "seed", "topic": "אבחון,קודי שגיאה", "equipment": "DX300,DX340,DX380,DX27,DX35,DX62", "symptom": "קודי שגיאה DOOSAN-Net", "brand": "Doosan"}
    },
    {
        "id": "doosan_mini_excavator_001",
        "text": (
            "מחפרוני מיני דוסאן — DX27Z / DX35Z / DX62R — תקלות נפוצות\n\n"
            "מאפיינים כלליים:\n"
            "• DX27Z: מנוע Yanmar 3TNV88 (18.8 kW), Zero Tail Swing\n"
            "• DX35Z: מנוע Yanmar 3TNV88C (24.4 kW), Zero Tail Swing\n"
            "• DX62R: מנוע Doosan D24 (33.8 kW), Reduced Tail Swing\n\n"
            "1. מחפרון לא נוסע (No Travel)\n"
            "   סיבה שכיחה: לחץ Pilot לא מגיע לשסתומי הנסיעה.\n"
            "   בדיקה: בדוק שסתום Pilot Safety (Safety Lever Lock Valve) — רוב הדגמים דורשים שמוט הבטיחות יורד.\n"
            "   בדיקה נוספת: בדוק פילטר Pilot (ב-DX35Z נמצא מאחורי לוח השמאלי).\n"
            "   פתרון: החלף פילטר Pilot כל 500 שעות.\n\n"
            "2. Dozer Blade לא מרים (ב-DX35Z ו-DX62R)\n"
            "   סיבה: שסתום גלינדר ה-Blade תקוע.\n"
            "   בדיקה: בדוק לחץ על קו הגלינדר — צריך ~200 bar לפחות.\n"
            "   פתרון: נקה שסתום, בדוק O-rings בגלינדר.\n\n"
            "3. רעש גבוה ממנוע Yanmar\n"
            "   DX27/DX35 מצוידים ב-Yanmar — רעש גבוה = מסנן אוויר סתום.\n"
            "   בדוק AIR CLEANER — ב-DX27 נמצא מתחת ל-Hood ימין.\n\n"
            "4. כוח מופחת בזרוע (Arm / Stick Weak)\n"
            "   ב-DX62R: בדוק שסתום Arm Relief (מוגדר ל-280 bar).\n"
            "   בדוק שחיקת גלינדר Arm — פרק ובדוק אטמים (Seals).\n\n"
            "5. דליפת שמן ממפרק (Pin Seal Leak)\n"
            "   מיני מחפרונים רגישים לדליפות ב-Pin Seals בגלל עבודה קרובה לאדמה.\n"
            "   בדוק ושמן כל Grease Point כל 50 שעות.\n"
            "   Grease Points: Boom Foot Pin, Boom Cylinder Rod Pin, Arm Cylinder, Bucket Pins."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,מנוע", "equipment": "DX27,DX35,DX62", "symptom": "תקלות מיני מחפרון", "brand": "Doosan"}
    },
    {
        "id": "doosan_wheel_loader_001",
        "text": (
            "מעמיסי גלגלים דוסאן — DL300 / DL380 / DL420 — מערכת הנעה ותיבת הילוכים\n\n"
            "דגמים ומנועים:\n"
            "• DL300: מנוע Doosan DL06K (120 kW)\n"
            "• DL380: מנוע Doosan DL06P (153 kW)\n"
            "• DL420: מנוע Doosan DL08 (186 kW)\n"
            "תיבת הילוכים: ZF Powershift 4-speed automatic\n\n"
            "1. תיבת הילוכים לא עוברת הילוך (Transmission Shift Failure)\n"
            "   קוד שגיאה טיפוסי: TC fault / ZF Transmission Fault\n"
            "   בדיקה: בדוק מפלס שמן תיבת הילוכים (Dip Stick — מנוע סרק).\n"
            "   בדיקה: חבר סורק ZF TestMan לאיתור קוד שגיאה מדויק.\n"
            "   פתרון: אם שמן נמוך — מלא שמן ZF Ecofluid M. אם TCU fault — איפוס ובדיקה.\n\n"
            "2. מעמיס לא מרים זרוע (Lift Arm Weak)\n"
            "   ב-DL420 עם שסתום עומס (Load Sensing Valve):\n"
            "   בדיקה: בדוק לחץ Lift Relief — נומינלי 250 bar.\n"
            "   בדוק: מסנן הידראולי (החלף כל 500 שעות).\n\n"
            "3. היגוי כבד (Steering Heavy)\n"
            "   מעמיסי גלגלים עם היגוי אורביטרולי (Orbitrol Steering).\n"
            "   בדיקה: לחץ משאבת היגוי — צריך ~170–200 bar בתפוקה מלאה.\n"
            "   פתרון: כוונן שסתום Relief היגוי. אם לא עוזר — החלף משאבת היגוי.\n\n"
            "4. בלמים חלשים (Wet Disc Brake Wear)\n"
            "   DL380/DL420 מצוידים בבלמי דיסק רטובים (Wet Disc Brakes) בציר.\n"
            "   סיבה: שמן בלמים (Axle Oil) מזוהם או מפלס נמוך.\n"
            "   בדיקה: פרק בורג בדיקה בציר — שמן צריך לצאת נקי.\n"
            "   פתרון: החלף שמן ציר (SAE 80W-90 GL-5) כל 1000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "תיבת הילוכים,הנעה,היגוי", "equipment": "DL300,DL380,DL420", "symptom": "תקלות מעמיס גלגלים", "brand": "Doosan"}
    },
    {
        "id": "doosan_engine_dseries_001",
        "text": (
            "מנועי D-Series של דוסאן/דוולון — תחזוקה ותקלות\n\n"
            "סדרת מנועי D-Series: D18, D24, DL06, DL08, DB58\n"
            "שימוש: מחפרוני DX180–DX800, מעמיסי DL200–DL550\n\n"
            "מאפיינים כלליים: Common Rail Injection (CRI) — Bosch, Turbocharger עם Intercooler, "
            "EGR (Exhaust Gas Recirculation) ב-Stage V, DPF (Diesel Particulate Filter) ב-Stage V\n\n"
            "1. מנוע מאבד הספק (Power Loss) — Derate Mode\n"
            "   סיבה שכיחה: DPF סתום (Soot Level High).\n"
            "   פתרון: בצע Regeneration אוטומטית — הפעל בגז גבוה (High Idle) לפחות 45 דקות ללא עומס.\n"
            "   אם לא עוזר: ריג'נרציה פורסת בסדנה (Forced DPF Regen) עם סורק אבחון.\n\n"
            "2. עשן שחור (Black Smoke) ממנוע D-Series\n"
            "   סיבה: Injector פגום, מסנן אוויר סתום, Turbo לא עובד.\n"
            "   בדיקה: בדוק Boost Pressure ב-Intercooler Outlet — ב-DL06 צריך ~1.8 bar בעומס.\n"
            "   פתרון: בדוק צינורות Intercooler לדליפות, בדוק Turbo לחופשיות סיבוב.\n\n"
            "3. מנוע רועד בסרק (Rough Idle)\n"
            "   סיבה: Injector אחד או יותר פגומים, לחץ Common Rail נמוך.\n"
            "   בדיקה: עם תוכנת Doosan Engine Diagnostics — בצע Cylinder Balance Test.\n\n"
            "4. Glow Plugs (נרות להט) ב-DX35/DX62\n"
            "   תסמין: קשה להתנעה בקור.\n"
            "   בדיקה: מד נגד/אוהמטר — כל Plug צריך 0.5–2 אוהם. אינסוף = שבור.\n\n"
            "5. EGR Valve תקוע פתוח (DX300 Stage IV)\n"
            "   תסמין: עשן לבן-אפור, צריכת דלק גבוהה, הספק נמוך.\n"
            "   פתרון: פרק ונקה EGR Valve עם ממס פחמן (Carbon Cleaner). אם שחוק — החלף.\n\n"
            "תחזוקה:\n"
            "שמן מנוע D-Series: VDS-4.5 — החלפה כל 500 שעות.\n"
            "מסנן שמן: החלפה עם שמן. V-belts: בדיקת מתח ושחיקה כל 500 שעות."
        ),
        "metadata": {"source": "seed", "topic": "מנוע,D-Series,DPF,EGR", "equipment": "DX300,DX380,DL380,DL420", "symptom": "תקלות מנוע D-Series", "brand": "Doosan"}
    },
    {
        "id": "doosan_swing_motor_001",
        "text": (
            "מנוע סיבוב (Swing Motor) — DX300 / DX340 / DX380 — אבחון מעמיק\n\n"
            "מנוע הסיבוב ב-DX300 מסוג Piston Motor עם גיר Swing Reduction.\n\n"
            "1. סיבוב חד צדדי (Swings Better One Side)\n"
            "   בדיקה: חבר מד לחץ לנקודות A ו-B של Swing Motor (Clockwise / Counter-CW).\n"
            "   לחץ נומינלי: ~260–280 bar בשני הכיוונים.\n"
            "   פתרון: כוונן Swing Relief Valves בנפרד לשני הכיוונים.\n\n"
            "2. סיבוב 'מקפץ' (Jerky Swing)\n"
            "   סיבה: שסתומי Make-Up (Anti-Void Valves) פגומים.\n"
            "   תפקיד Make-Up Valve: מלא חלל שנוצר בעצירת סיבוב מהירה.\n"
            "   פתרון: נקה Make-Up Valve Check Ball.\n\n"
            "3. Swing Brake לא עובד (No Parking Brake)\n"
            "   ב-DX300 בלם החנייה של הסיבוב הוא Spring Apply, Hydraulic Release.\n"
            "   תסמין: הכלי מסתובב בנסיעה בשיפוע.\n"
            "   בדיקה: לחץ Pilot Release ל-Brake = 35 bar. בדוק שלחץ Pilot תקין.\n"
            "   פתרון: החלף Swing Parking Brake Valve.\n\n"
            "4. שמן Swing Gear Box דולף\n"
            "   שמן: SAE 90 EP Gear Oil. החלפה: כל 2000 שעות.\n"
            "   סכנה: שמן נמוך = שחיקת גלגלי Planet בגיר הפחתה.\n\n"
            "5. רעש גריסה מה-Swing Ring Gear\n"
            "   Swing Ring Gear = טבעת שיניים חיצונית מתחת לבית.\n"
            "   שימון: גריז מיוחד (Open Gear Grease) כל 250 שעות דרך נקב הגריז."
        ),
        "metadata": {"source": "seed", "topic": "סיבוב,Swing Motor", "equipment": "DX300,DX340,DX380", "symptom": "תקלות מנוע סיבוב", "brand": "Doosan"}
    },
    {
        "id": "bobcat_skid_steer_fault_codes_001",
        "text": (
            "קודי תקלה (B-Codes) בסקיד סטיר בובקט — S570 / S650 / S770 / T650 / T770\n\n"
            "בובקט שייכת לדוסאן (Doosan Bobcat) מאז 2007. מערכת האבחון משתמשת ב-B-Codes.\n\n"
            "גישה לקודי שגיאה:\n"
            "1. כנס לתא המפעיל, סגור את הדלת.\n"
            "2. הורד את Safety Bar (מוט הבטיחות).\n"
            "3. הפעל מתג הצתה ל-ON (ללא הפעלת מנוע).\n"
            "4. הקש שלוש פעמות על כפתור Mode.\n"
            "5. קודי B יוצגו בלוח הדיגיטלי.\n\n"
            "קודי B נפוצים:\n"
            "B-2-1 — תקלת חיישן מיקום זרוע (Lift Arm Position Sensor)\n"
            "   פתרון: בדוק חיישן מיקום זרוע (Potentiometer) — ממוקם בציר הזרוע.\n\n"
            "B-3-1 — תקלת חיישן מיקום Bob-Tach (Attachment Coupler Sensor)\n"
            "   פתרון: בדוק מיקרוסוויץ' ב-Bob-Tach, נקה מלכלוך.\n\n"
            "B-4-2 — תקלת מנוע הידראולי ימין (Right Drive Motor Fault)\n"
            "   תסמין: כלי נוסע שמאלה בלבד, עיגול בנסיעה.\n\n"
            "B-5-1 — תקלת מנוע מאוורר (Fan Motor Fault)\n"
            "   פתרון: בדוק מנוע מאוורר מנוע, בדוק רלאי מאוורר.\n\n"
            "B-6-3 — תקלת חיישן טמפרטורת הידראוליקה גבוהה מדי\n"
            "   פתרון: נקה Oil Cooler, בדוק מפלס שמן הידראולי.\n\n"
            "B-7-1 — תקלת BCS (Bobcat Control System) — CAN Communication Error\n"
            "   פתרון: בדוק תקינות כבל CAN בין בקרים. בדוק 120 אוהם בין CAN-H ל-CAN-L.\n\n"
            "איפוס קודים: לאחר תיקון — כבה לחלוטין, המתן 30 שניות, הפעל."
        ),
        "metadata": {"source": "seed", "topic": "קודי שגיאה,B-Codes", "equipment": "S570,S650,S770,T650,T770", "symptom": "קודי תקלה בובקט", "brand": "Bobcat"}
    },
    {
        "id": "bobcat_skid_steer_drive_001",
        "text": (
            "מנועי הנעה הידרוסטטיים בסקיד סטיר בובקט — תקלות ואבחון\n\n"
            "דגמים: S570, S650, S770, T650 (מסילות), T770 (מסילות)\n"
            "מערכת ההנעה: Hydrostatic Drive — משאבת Tandem Hydrostatic Pump + שני מנועי Drive Motor\n\n"
            "1. כלי נוסע עקום (Pulls to One Side)\n"
            "   פתרון: ב-S650 — כנס לתפריט Operator Mode וכייל מחדש יחסי ג'ויסטיק/נסיעה.\n"
            "   פתרון אחר: בדוק שמנוע ימין ושמאל מייצרים ספיקה שווה. בדוק שסתומי Charge Relief (250 bar).\n\n"
            "2. כלי לא נוסע בכלל (No Drive)\n"
            "   בדוק: לחץ Charge Pressure = 27–30 bar. אם נמוך = Charge Pump פגומה.\n"
            "   בדוק: Safety Interlock — מוט הבטיחות חייב להיות למטה!\n"
            "   בדוק: קוד B-4-2 / B-4-3 (תקלת מנוע נסיעה).\n\n"
            "3. נסיעה איטית / חסר כוח (Sluggish Drive)\n"
            "   בדיקה: מד לחץ בנקודת Work Port של המשאבה — צריך ~420 bar בעומס מלא.\n"
            "   פתרון: בדוק Case Drain Flow — זרימת שמן גבוהה דרך Case Drain = שחיקת פיסטונים.\n\n"
            "4. מסילות T650/T770 — מתח מסילה\n"
            "   מסילות גומי (Rubber Tracks) דורשות מתח של ~50–80 mm רפיון.\n"
            "   כוונון: ב-T650 — נקב גריז ב-Idler Tensioner. מלא גריז עד קבלת מתח נכון.\n"
            "   מסילה רפויה = נפילת מסילה בפניות חדות.\n\n"
            "5. Heat Build-Up בנסיעה ממושכת\n"
            "   נקה את ה-Hydraulic Oil Cooler מקש ואבק.\n"
            "   בדוק מפלס שמן הידראולי. ב-S770 קיבולת = 33 ליטר.\n"
            "   שנה שמן הידראולי כל 1000 שעות (AW 46 Hydraulic Oil)."
        ),
        "metadata": {"source": "seed", "topic": "הנעה הידרוסטטית,מסילות", "equipment": "S570,S650,S770,T650,T770", "symptom": "תקלות נסיעה סקיד סטיר", "brand": "Bobcat"}
    },
    {
        "id": "bobcat_lift_arm_001",
        "text": (
            "זרוע הרמה (Lift Arm) בסקיד סטיר בובקט — תקלות ותחזוקה\n\n"
            "דגמים: S570, S650, S770, T650, T770\n"
            "סוג זרוע: Vertical Lift (הרמה אנכית) — S570/S650/T650. Radius Lift — S770/T770.\n\n"
            "1. זרוע עולה לאט (Slow Lift)\n"
            "   בדיקה: לחץ Relief של מעגל הרמה — נומינלי 230–260 bar.\n"
            "   בדיקה: מסנן הידראולי — אם סתום = ירידת ספיקה.\n\n"
            "2. זרוע יורדת לאחר הרמה (Arm Drifts Down)\n"
            "   סיבה: אטמי גלינדר הרמה שחוקים (Lift Cylinder Seals).\n"
            "   בדיקה: הרם זרוע לגובה מקסימלי, כבה מנוע — מדוד ירידה. יותר מ-15mm בשעה = החלף אטמים.\n"
            "   סיבה אחרת: שסתום Anti-Drift (Hold Valve) דולף.\n\n"
            "3. רעש 'פטיש' בעת הגעה לגובה מקסימלי\n"
            "   ב-S650 — Load Sensing Relief Valve מכוון גבוה מדי.\n"
            "   פתרון: כוונן Lift Relief Valve ל-240 bar.\n\n"
            "4. כשל ב-Float Mode\n"
            "   Float Mode = זרוע צפה ומתאימה לפני השטח.\n"
            "   ב-S770: Float לא עובד — בדוק שסתום Float Control, בדוק כבל/חיבור לכפתור בג'ויסטיק.\n\n"
            "5. Lift Arm Pivot Pins שחוקים\n"
            "   תסמין: רעשן בבסיס הזרוע, תנועה לא יציבה.\n"
            "   שימון: כל 50 שעות עם Moly Grease (גריז מוליבדן).\n"
            "   סכנה: Pivot Pin שבור = קריסת זרוע!\n\n"
            "6. Bob-Tach לא נועל\n"
            "   Bob-Tach = מערכת החלפת אביזרים מהירה.\n"
            "   בדיקה: בדוק שסתום הידראולי של Bob-Tach Lock Cylinder.\n"
            "   בדוק Safety Lock Switch — מונע שחרור בלתי מכוון."
        ),
        "metadata": {"source": "seed", "topic": "זרוע הרמה,Bob-Tach", "equipment": "S570,S650,S770,T650,T770", "symptom": "תקלות זרוע הרמה סקיד סטיר", "brand": "Bobcat"}
    },
    {
        "id": "bobcat_mini_excavator_001",
        "text": (
            "מחפרוני מיני בובקט — E35 / E50 / E85 — תקלות נפוצות\n\n"
            "מאפיינים:\n"
            "• E35: מנוע Kubota D1803 (18.1 kW), Zero Tail Swing\n"
            "• E50: מנוע Kubota V2607 (28.9 kW), Reduced Tail Swing\n"
            "• E85: מנוע Doosan D24 (43.2 kW), Conventional Swing\n\n"
            "1. E35 — מנוע Kubota לא עולה\n"
            "   בדוק: Fuel Shutoff Solenoid — ב-E35 ממוקם על גבי משאבת הדלק.\n"
            "   בדוק: Safety Bar חייב להיות מורד.\n"
            "   בדוק: מסנן דלק — Kubota רגיש לדלק מזוהם.\n\n"
            "2. E50 — חוסר כוח בחפירה\n"
            "   בדוק: Main Relief Pressure ב-E50 = 310 bar.\n"
            "   ב-E50 עם שסתום AUX: ודא שה-AUX Flow לא 'גונב' ספיקה מהחפירה.\n"
            "   בדוק: מסנן Pilot (Pilot Filter) כל 500 שעות.\n\n"
            "3. E85 — Swing איטי לצד אחד\n"
            "   בדוק: Swing Relief Pressure כל 250–280 bar (אחיד בשני הכיוונים).\n\n"
            "4. E35/E50 — רטט Dozer Blade בנסיעה\n"
            "   סיבה: שסתום Blade Hold (Anti-Drift) לא חוסם את הגלינדר.\n"
            "   פתרון: נקה/החלף Blade Hold Valve.\n\n"
            "5. E85 — AUX Hydraulics (לפטיש/גריפר) חלשים\n"
            "   בדוק: AUX Flow Setting — ב-E85 ניתן לכוונן ספיקה AUX בלוח הבקרה.\n"
            "   בדוק: AUX Relief Pressure — 210 bar.\n\n"
            "Grease Points חובה — כל 50 שעות:\n"
            "E35: Boom Cylinder Base, Boom Pivot, Stick Pin, Bucket Pin, Dozer Blade Pins.\n"
            "E50/E85: נוסף Swing Bearing — גריז כל 250 שעות."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,מנוע", "equipment": "E35,E50,E85", "symptom": "תקלות מיני מחפרון בובקט", "brand": "Bobcat"}
    },
    {
        "id": "doosan_travel_system_001",
        "text": (
            "מערכת נסיעה (Travel System) — DX300 / DX380 — אבחון מתקדם\n\n"
            "מערכת הנסיעה כוללת: Travel Motor + Planetary Gear + Final Drive + Sprocket + Track.\n\n"
            "לחצים נומינליים:\n"
            "• Travel High Pressure (Work): 420 bar\n"
            "• Travel Pilot Pressure: 35–38 bar\n"
            "• Case Drain Pressure: פחות מ-3 bar\n\n"
            "1. כלי לא נוסע אחד צד (One Side No Travel)\n"
            "   בדיקה שלב א: בדוק Travel Pilot Pressure — חייב להגיע לשסתום הנסיעה הרלוונטי.\n"
            "   בדיקה שלב ב: חבר מד לחץ לנקודת Work Port של Travel Motor (A/B Port).\n"
            "   אם לחץ A/B נמוך = שסתום Travel Counterbalance Valve חסום.\n"
            "   פתרון: פרק ונקה את ה-Counterbalance Valve (Travel Brake Valve).\n\n"
            "2. כלי נוסע איטי (Slow Travel Both Sides)\n"
            "   בדיקה: High/Low Speed Mode — בדוק שלחצן Speed (Tortoise/Rabbit) עובד.\n"
            "   ב-High Speed: Travel Motor משנה Displacement לקטן = מהיר יותר.\n"
            "   קוד שגיאה: E0502 = תקלת חיישן Swash Plate (Displacement Control).\n\n"
            "3. Counterbalance Valve תקוע (ב-DX300)\n"
            "   תסמין: כלי 'בורח' בשיפוע למטה = Counterbalance לא חוסם.\n"
            "   תסמין הפוך: כלי לא נוסע = Counterbalance תקוע סגור.\n"
            "   פתרון: פרק, נקה, החלף O-rings בשסתום.\n\n"
            "4. Case Drain חם ומוגבר\n"
            "   אם ספיקת Case Drain גבוהה מ-8 L/min = שחיקת פיסטונים ב-Motor.\n"
            "   פתרון: מדוד ספיקה בצינור Case Drain עם Flow Meter.\n\n"
            "5. Track Adjustment (כוונון מתח זחל) ב-DX300\n"
            "   מתח נכון: 30–40mm רפיון בין Idler לזחל במרכז.\n"
            "   שחרור מתח: פרק בורג Grease Relief לשחרור גריז."
        ),
        "metadata": {"source": "seed", "topic": "נסיעה,Travel System", "equipment": "DX300,DX380", "symptom": "תקלות מערכת נסיעה מחפרון", "brand": "Doosan"}
    },
    {
        "id": "doosan_wheel_loader_maintenance_001",
        "text": (
            "לוח תחזוקה — מעמיסי גלגלים דוסאן DL300 / DL380 / DL420\n\n"
            "תחזוקה יומית (לפני כניסה לעבודה):\n"
            "• רמת שמן מנוע — מוט בליעה בין MIN ל-MAX\n"
            "• רמת קירור מנוע — בצנצנת הרחבה\n"
            "• שמן הידראולי — Sight Glass על גבי הטנק\n"
            "• שמן תיבת הילוכים ZF — Dipstick עם מנוע סרק\n"
            "• לחץ צמיגים: L3 = 3.5 bar קדמי, 3.2 bar אחורי\n\n"
            "תחזוקה כל 250 שעות:\n"
            "• החלף שמן מנוע ופילטר שמן (15W-40 ACEA E7 בדרך כלל)\n"
            "• החלף מסנן דלק ראשי + Water Separator\n"
            "• בדוק מסנן אוויר — נקה או החלף\n"
            "• שמן כל נקודות הגריז: זרוע, מפרקי היגוי, צירי כוונון\n\n"
            "תחזוקה כל 500 שעות:\n"
            "• החלף פילטר הידראולי (Return Filter + Suction Strainer)\n"
            "• בדוק שמן ZF Transmission — אם שחור/נשרף, החלף מוקדם\n\n"
            "תחזוקה כל 1000 שעות:\n"
            "• החלף שמן הידראולי (AW 46 Hydraulic Oil)\n"
            "• החלף שמן ZF Transmission (ZF Ecofluid M / LifeGuard Fluid 6)\n"
            "• החלף שמן צירים (Axle Oil — SAE 80W-90 GL-5)\n\n"
            "תחזוקה כל 2000 שעות:\n"
            "• החלף שמן ציר קדמי ואחורי\n"
            "• בדוק Turbocharger — ניקוי ובדיקת חופשיות ציר\n\n"
            "תחזוקה מיוחדת — DPF (DL380/DL420 Stage V):\n"
            "• Regeneration אוטומטית: כל 8–12 שעות עבודה\n"
            "• אם מנורת DPF דולקת: בצע Parked Regen\n"
            "• החלף DPF כל 6000 שעות עבודה ב-DL420"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה,לוח שירות", "equipment": "DL300,DL380,DL420", "symptom": "לוח תחזוקה מעמיס גלגלים", "brand": "Doosan"}
    },
    {
        "id": "bobcat_skid_steer_chain_belt_001",
        "text": (
            "מערכת שרשראות הנעה פנימית (Drive Chain) — S570 / S650 — תחזוקה ותקלות\n\n"
            "בדגמי S570 ו-S650 (סקיד סטיר גלגלים), מנועי ההנעה ההידרוסטטיים מניעים גלגלים דרך שרשראות פנימיות.\n"
            "מיקום: השרשראות ממוקמות בתוך ה-Chassis בשני הצדדים — גישה דרך דלת צד.\n\n"
            "1. בדיקת מתח שרשרת (Chain Tension)\n"
            "   לחץ על השרשרת במרכז — רפיון מקסימלי: 12–18 mm.\n"
            "   שרשרת רפויה מדי: גורמת לרעש וחיכוך בתוך תא ה-Chassis.\n"
            "   כוונון: שחרר ברגי ה-Idler Sprocket, הזזה + הדק.\n\n"
            "2. תסמינים לשרשרת שחוקה/קרועה\n"
            "   רעש 'חריקה' מצד אחד של הכלי בנסיעה.\n"
            "   כלי נוסע עקום ללא סיבה הידראולית.\n"
            "   פתאום — צד אחד לא נוסע בכלל (שרשרת קרועה).\n\n"
            "3. שימון שרשרת (Chain Lubrication)\n"
            "   שמן שרשרת (Chain Lube Spray — Dry Type) כל 250 שעות.\n"
            "   אל תשתמש בגריז סמיך — מצטבר לכלוך ומחיש שחיקה.\n\n"
            "4. Sprocket שחוק\n"
            "   תסמין: שרשרת 'קופצת' על ה-Sprocket, רעש בלתי רגיל.\n"
            "   בדיקה: בדוק שיניים של Sprocket — שיניים 'מחודדות' = שחוקות = החלף.\n"
            "   המלצה: החלף שרשרת ו-Sprocket ביחד תמיד.\n\n"
            "5. שיפוצי ציר גלגל (Wheel Hub Seal)\n"
            "   תסמין: שמן זולג מאחורי גלגל.\n"
            "   סיבה: אטם ציר (Hub Seal) שחוק — שמן הידרוסטטי דולף לתוך ה-Chassis = סכנה!\n"
            "   פתרון: פרק גלגל, החלף Hub Seal."
        ),
        "metadata": {"source": "seed", "topic": "שרשרת הנעה,מסילות", "equipment": "S570,S650,T650,T770", "symptom": "תקלות שרשרת הנעה סקיד סטיר", "brand": "Bobcat"}
    },
    {
        "id": "doosan_excavator_maintenance_schedule_001",
        "text": (
            "לוח תחזוקה מפורט — מחפרוני דוסאן/דוולון DX300 / DX340 / DX380\n\n"
            "תחזוקה לפני כל משמרת (יומי):\n"
            "• בדוק שמן מנוע (Doosan D-Series) — Dipstick\n"
            "• בדוק מפלס קירור מנוע — Reservoir\n"
            "• בדוק שמן הידראולי — Sight Glass בטנק (טמפ' קרה)\n"
            "• נקה Water Separator / Fuel Pre-Filter\n"
            "• בדוק מסנן אוויר — אינדיקטור ירוק = תקין\n"
            "• בדוק מתח זחלים ומצב Sprocket\n"
            "• שמן Grease Points יומיים: Bucket Pin, Stick Pin, Boom Pin\n\n"
            "תחזוקה כל 50 שעות:\n"
            "• גריז כל Boom Cylinder Rod Pins, Stick Cylinder Pins, Bucket Cylinder Pins\n"
            "• גריז Idler Pins\n"
            "• בדוק Track Shoes — הדק ברגים רופפים (Torque: 500 Nm ב-DX300)\n\n"
            "תחזוקה כל 250 שעות:\n"
            "• החלף שמן מנוע + פילטר שמן (Doosan Spec: 15W-40 CK-4)\n"
            "• החלף מסנן דלק ראשי\n"
            "• גריז Swing Bearing (Grease: Mobil XHP 222 או שווה ערך)\n"
            "• בדוק רדיאטור ו-Oil Cooler — נקה\n\n"
            "תחזוקה כל 500 שעות:\n"
            "• החלף פילטר הידראולי ראשי (Return Filter) — חלק Doosan 400404-00241\n"
            "• החלף פילטר Pilot (10 מיקרון)\n"
            "• בדוק Fuel Injectors עם Doosan DDT (Balance Test)\n\n"
            "תחזוקה כל 1000 שעות:\n"
            "• החלף שמן הידראולי (ISO VG 46 או VG 68 לפי סביבה)\n"
            "• החלף שמן Swing Gear Box (SAE 90 EP)\n"
            "• בדוק Final Drive Oil — שני הצדדים (SAE 80W-90 GL-4)\n\n"
            "תחזוקה כל 2000 שעות:\n"
            "• החלף שמן Final Drive (שני הצדדים)\n"
            "• החלף Suction Strainer (מסנן שאיבה של טנק)\n"
            "• בדוק Engine Valve Clearance"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה,לוח שירות", "equipment": "DX300,DX340,DX380", "symptom": "לוח תחזוקה מחפרון דוסאן", "brand": "Doosan"}
    },
    {
        "id": "bobcat_mini_excavator_maintenance_001",
        "text": (
            "תחזוקה מניעתית — מחפרוני מיני בובקט E35 / E50 / E85\n\n"
            "E35 (מנוע Kubota D1803):\n"
            "• שמן מנוע: Kubota Super UDT2 או 15W-40 CK-4\n"
            "• החלפת שמן: כל 200 שעות\n"
            "• מסנן אוויר: בדוק כל 50 שעות, החלף כל 250 שעות\n"
            "• קירור: Kubota Super Coolant — החלף כל 1000 שעות\n"
            "• גריז: Boom Pin, Stick Pin, Bucket Pin, Blade Pins כל 50 שעות\n\n"
            "E50 (מנוע Kubota V2607):\n"
            "• שמן מנוע: 15W-40 API CK-4 — החלף כל 250 שעות\n"
            "• Fuel Filter ראשי: כל 250 שעות\n"
            "• Pilot Filter: כל 500 שעות\n"
            "• שמן הידראולי: ISO VG 46 — החלף כל 1000 שעות\n"
            "• Swing Bearing: גריז כל 250 שעות\n\n"
            "E85 (מנוע Doosan D24):\n"
            "• שמן מנוע: 15W-40 ACEA E7/E9 — כל 250 שעות\n"
            "• DPF: E85 Stage V — Regeneration אוטומטית\n"
            "• Final Drive: שמן SAE 80W-90 — החלף כל 1000 שעות\n\n"
            "נקודות גריז כלל הדגמים (NLGI #2 Lithium Complex Grease):\n"
            "1. Boom Foot Pin (2 נקבים)\n"
            "2. Boom Cylinder Base Pin\n"
            "3. Boom Cylinder Rod Pin\n"
            "4. Arm (Stick) Pivot Pin\n"
            "5. Arm Cylinder Base + Rod Pins\n"
            "6. Bucket Pin + Linkage Pins\n"
            "7. Dozer Blade Cylinder Pin (E35/E50)\n"
            "8. Swing Bearing (E50/E85)"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה,גריז,שמנים", "equipment": "E35,E50,E85", "symptom": "לוח תחזוקה מחפרון מיני בובקט", "brand": "Bobcat"}
    },
    {
        "id": "doosan_wheel_loader_hydraulic_001",
        "text": (
            "מערכת הידראוליקה — מעמיסי גלגלים DL300 / DL380 / DL420 — תקלות ואבחון\n\n"
            "מערכת הידראוליקה במעמיס גלגלים דוסאן כוללת:\n"
            "• משאבה הידראולית Gear Pump / Piston Pump (Load Sensing בדגמי DL380/DL420)\n"
            "• בלוק שסתומים ראשי (Main Control Valve)\n"
            "• גלינדרי הרמה (Lift Cylinders) — 2 גלינדרים בשני צידי הזרוע\n"
            "• גלינדר הטיה (Tilt Cylinder)\n"
            "• מערכת היגוי (Orbitrol Steering)\n\n"
            "1. דלי לא מרים (No Lift)\n"
            "   בדיקה: בדוק לחץ Lift Circuit — DL380 = 240 bar נומינלי.\n"
            "   פתרון: כוונן Lift Relief Valve. אם לא עוזר — פרק ונקה Main Control Valve.\n\n"
            "2. הדלי לא נוטה (No Tilt)\n"
            "   בדיקה: בדוק Tilt Circuit Pressure — 220 bar.\n"
            "   בדיקה: בדוק Tilt Spool במסדרת השסתומים.\n\n"
            "3. שמן הידראולי גולש מהטנק בעת עבודה\n"
            "   סיבה: מסנן חזרה (Return Filter) סתום — שמן עוקף דרך By-Pass.\n"
            "   בדיקה: אינדיקטור Return Filter על לוח — אם אדום = החלף.\n"
            "   פתרון: החלף Return Filter (ב-DL420 = Doosan 400404-00283).\n\n"
            "4. היגוי כבד בקצוות (Steering Stiff at Full Lock)\n"
            "   ב-DL300: Steering Relief = 175 bar.\n"
            "   פתרון: כוונן Steering Relief Valve. בדוק גם Orbitrol Steering Unit לשחיקה.\n\n"
            "5. זרוע 'רועדת' בהרמה\n"
            "   ב-DL380 עם Load Sensing: תנודת לחץ = Pressure Oscillation.\n"
            "   פתרון: כוונן LS Damping Valve בגוף המשאבה (דורש טכנאי מוסמך)."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,מעמיס", "equipment": "DL300,DL380,DL420", "symptom": "תקלות הידראוליקה מעמיס גלגלים", "brand": "Doosan"}
    },
    {
        "id": "bobcat_electrical_system_001",
        "text": (
            "מערכת חשמל ואלקטרוניקה — בובקט S650 / S770 / T770 — אבחון\n\n"
            "מערכת הבקרה האלקטרונית של בובקט מבוססת על BCS (Bobcat Control System) — מחברת:\n"
            "• ECM (Engine Control Module) — בקר המנוע\n"
            "• MCM (Machine Control Module) — בקר המכונה\n"
            "• DDM (Display / Instrument Module) — לוח מכשירים\n\n"
            "1. מנוע לא מתניע (No Start) — S650\n"
            "   בדוק מתח סוללה: מינימום 12.4V.\n"
            "   בדוק Safety Interlock System: דלת סגורה? Safety Bar למטה? Seat Belt (ב-S770)?\n"
            "   בדוק קוד שגיאה: B-1-1 = Safety Interlock Open.\n"
            "   בדוק ממסר ראשי (Main Relay) ואת ה-Fusible Link.\n\n"
            "2. לוח מכשירים כבה תוך כדי עבודה\n"
            "   סיבה: קוד B-7-1 = CAN Communication Loss.\n"
            "   בדוק כבל CAN בין MCM ל-DDM.\n"
            "   בדוק מחברים — ניקוי עם Electronics Contact Cleaner.\n"
            "   בדוק הארקה (Ground Straps) בין Chassis למנוע.\n\n"
            "3. מנוע עולה אך ACS לא עובד\n"
            "   ACS = הורדת סרק אוטומטית כאשר ג'ויסטיקים ב-Neutral 5 שניות.\n"
            "   בדיקה: בדוק חיישן מיקום Joystick (Hall Effect Sensor).\n"
            "   פתרון: כייל מחדש Joystick עם תוכנת Bobcat Service Analyzer.\n\n"
            "4. נורת Charge Battery דולקת\n"
            "   בדוק מתח טעינה: מולטימטר בין קטבי סוללה עם מנוע דולק = 13.8–14.4V.\n"
            "   בדוק רצועת אלטרנטור (Drive Belt).\n\n"
            "5. מפסק בטיחות מושב (Seat Bar / Restraint Bar Switch)\n"
            "   תסמין: ג'ויסטיקים לא מגיבים גם כשמוט הבטיחות למטה.\n"
            "   בדוק: מיקרוסוויץ' של Safety Bar — מכוסה בלכלוך ולא נלחץ עד הסוף.\n"
            "   ב-T770: Seat Belt Switch נוסף — בדוק כי חגור."
        ),
        "metadata": {"source": "seed", "topic": "חשמל,אלקטרוניקה,BCS", "equipment": "S650,S770,T770", "symptom": "תקלות חשמל בובקט", "brand": "Bobcat"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Doosan/Bobcat entries. Total KB: {rag.count()} chunks")
