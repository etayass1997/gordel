"""Add Volvo knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "volvo_excavator_hydraulic_001",
        "text": (
            "תקלות הידראוליות נפוצות במחפרוני וולוו EC300/EC350/EC380\n\n"
            "מחפרוני הסדרה EC300 עד EC380 של וולוו (Volvo Construction Equipment) מצוידים במערכת הידראולית "
            "לחץ-משתנה (Load Sensing Hydraulic System) עם משאבת פיסטון (Piston Pump) מסוג A8VO.\n\n"
            "1. לחץ מערכת נמוך (Low System Pressure)\n"
            "   תסמינים: כלי חלש, תנועות איטיות, מנוע עמוס.\n"
            "   גורמים:\n"
            "   - שסתום Relief ראשי (Main Relief Valve) שחוק. לחץ תפעולי EC350 = 350 בר.\n"
            "   - משאבת Pilot (Pilot Pump) אינה מייצרת 35 בר — בדוק עם מד לחץ בנקודת בדיקה (TP1).\n"
            "   - צינור יניקה (Suction Hose) פגום — גורם לקאוויטציה (Cavitation) ונזק למשאבה.\n"
            "   בדיקה: חבר VCADS Pro, קרא פרמטרים של לחץ מערכת בזמן אמת.\n\n"
            "2. שמן הידראולי חם מדי (Oil Overheating)\n"
            "   גבול אזהרה: 90°C, גבול כיבוי: 100°C.\n"
            "   גורמים: מקרר שמן (Oil Cooler) סתום — נקה עם מים בלחץ נמוך מהצד הנגדי.\n"
            "   בדוק עם VCADS את טמפרטורת שמן בפרמטר MID 141 - SPN 3508.\n\n"
            "3. Arm/Boom איטי בצד אחד בלבד\n"
            "   גורם: שסתום כניסה (Load Check Valve) תקוע בבלוק השסתומים הראשי (MCV).\n"
            "   פתרון: פרק MCV, נקה ובדוק כדורי Check Valve, החלף O-rings ושסתומים שחוקים.\n\n"
            "הערה: תמיד השתמש בשמן הידראולי המאושר — Volvo Hydraulic Oil VG46 או VG68 בהתאם לאקלים."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "EC300,EC350,EC380", "symptom": "לחץ נמוך,שמן חם", "brand": "Volvo"}
    },
    {
        "id": "volvo_vcads_diagnostic_001",
        "text": (
            "מערכת אבחון VCADS Pro - מחפרוני וולוו ומכשירי צמה\n\n"
            "VCADS Pro (Volvo Component and Diagnostic System) היא תוכנת האבחון הרשמית של וולוו לכלי עבודה.\n\n"
            "חיבור למכשיר:\n"
            "1. הכנס מחבר OBD/Deutsch 9-pin לשקע האבחון (ליד מושב המפעיל).\n"
            "2. פתח VCADS Pro במחשב נייד.\n"
            "3. בחר את סוג הכלי (Machine Type) — לדוגמה EC350E.\n"
            "4. בחר MID (Message Identifier) הרלוונטי:\n"
            "   - MID 140 = בקר מנוע (Engine Control Unit)\n"
            "   - MID 141 = בקר הידראוליקה (Hydraulic Control Unit)\n"
            "   - MID 187 = בקר שידור/גיר (Transmission Control Unit)\n"
            "   - MID 253 = בקר מכונה (Machine Control Unit)\n\n"
            "קריאת קודי שגיאה — FMI (Failure Mode Identifier):\n"
            "- FMI 0 = ערך גבוה מדי (Above Normal Range)\n"
            "- FMI 1 = ערך נמוך מדי (Below Normal Range)\n"
            "- FMI 3 = מעגל פתוח/מתח גבוה (Voltage Above Normal)\n"
            "- FMI 4 = קצר לאדמה/מתח נמוך (Voltage Below Normal)\n"
            "- FMI 5 = מעגל פתוח (Open Circuit)\n"
            "- FMI 12 = רכיב פגום (Bad Intelligent Device)\n\n"
            "SPN (Suspect Parameter Number) נפוצים:\n"
            "- SPN 100 = לחץ שמן מנוע\n"
            "- SPN 110 = טמפרטורת קירור\n"
            "- SPN 3508 = טמפרטורת שמן הידראולי\n"
            "- SPN 168 FMI 1 = מתח סוללה נמוך — הסיבה הנפוצה ביותר לקודים מרובים בבת אחת"
        ),
        "metadata": {"source": "seed", "topic": "אבחון VCADS", "equipment": "EC300,EC350,EC380,L90,L110", "symptom": "אבחון כללי", "brand": "Volvo"}
    },
    {
        "id": "volvo_engine_d_series_001",
        "text": (
            "מנועי סדרת D של וולוו - תקלות ואבחון\n\n"
            "מחפרוני וולוו EC300-EC380 מצוידים במנוע D8K (8 ליטר) או D13K (13 ליטר) עם הזרקה ישירה "
            "(Common Rail Injection) ועמידה בתקן פליטה Stage V (אירופה) / Tier 4 Final (ארה\"ב).\n\n"
            "מאפייני מנוע D8K במחפרון EC350E:\n"
            "- הספק: 270 כ\"ס (201 קוט\"ש)\n"
            "- מומנט מרבי: 1380 ניוטון-מטר ב-1200 סל\"ד\n"
            "- Common Rail Pressure: 1800 בר בעומס מלא\n\n"
            "1. מנוע לא עולה — קוד FMI 12 ב-MID 140\n"
            "   גורם: מזרק (Injector) פגום או SCR לא מאותחל.\n"
            "   פתרון: הרץ Active Test להפעלת כל מזרק בנפרד. מזרק שלא מגיב = החלף.\n\n"
            "2. עשן כחול מהפלטה\n"
            "   גורם: שמן מנוע נשרף — אטמי שסתומים שחוקים, טורבו דולף שמן.\n"
            "   קוד אפשרי: SPN 2791 FMI 16 (EGR Valve).\n\n"
            "3. DPF (Diesel Particulate Filter) סתום\n"
            "   קוד: SPN 3251 — לחץ דיפרנציאלי ב-DPF גבוה.\n"
            "   פתרון: בצע Forced Regeneration דרך VCADS אם זמן עבודה מאפשר.\n"
            "   אם לא יצליח — יש להוציא DPF לניקוי מקצועי.\n\n"
            "4. DEF/AdBlue נמוך (Low Urea Level)\n"
            "   קוד: MID 140 SPN 1761 FMI 1.\n"
            "   תסמין: הודעה בצג, לאחר 10 שעות — Derate חמור.\n"
            "   פתרון: מלא מיכל AdBlue עם נוזל ISO 22241-1.\n\n"
            "תחזוקה מנוע D-Series:\n"
            "- שמן מנוע: VDS-4.5 — החלפה כל 500 שעות\n"
            "- Coolant: Volvo Coolant VCS2 — החלפה כל 2 שנים"
        ),
        "metadata": {"source": "seed", "topic": "מנוע D-Series", "equipment": "EC300,EC350,EC380", "symptom": "תקלות מנוע,DPF,AdBlue", "brand": "Volvo"}
    },
    {
        "id": "volvo_wheel_loader_l90_l110_001",
        "text": (
            "מטעינות גלגלים וולוו L90/L110/L120 - תקלות שידור וציר\n\n"
            "מטעינות הגלגלים L90H, L110H ו-L120H של וולוו מצוידות בתיבת הילוכים אוטומטית מסוג "
            "Volvo Powershift (MATRIS) עם ממשק CAN Bus לבקר TCU (MID 187).\n\n"
            "1. קופסת גיר לא עוברת הילוך (Transmission Won't Shift)\n"
            "   קוד: MID 187 SID 54 FMI 7 (Clutch Slip Detected).\n"
            "   גורם: בלאי Clutch Pack, לחץ הידראולי נמוך בקופסת הגיר.\n"
            "   בדיקה דרך VCADS: קרא MATRIS Fault Log.\n"
            "   פתרון: בדוק רמת שמן גיר (ATF). לחץ מינימלי בפנים: 14 בר.\n\n"
            "2. רעש חזק בנסיעה קדימה בהילוך 1\n"
            "   גורם: בלאי שיניים ב-Forward Low Clutch.\n"
            "   בדיקה: בצע Stall Test דרך VCADS — RPM בנקודת Stall גבוה מ-1750 = בעיה בגיר.\n\n"
            "3. הכלי לא נוסע כלל (No Drive)\n"
            "   בדוק: מנוף בחירת כיוון (FNR Lever) — שלח אות ל-TCU (בדוק ב-VCADS תחת MID 187 Parameter P1).\n"
            "   בדוק: Parking Brake Solenoid — אם לא משתחרר = כלי נעול.\n\n"
            "4. נעילת דיפרנציאל לא עובדת\n"
            "   קוד: MID 187 SPN 1421 FMI 5.\n"
            "   פתרון: בדוק סולנואיד, בדוק לחץ הידראולי על ציר.\n\n"
            "שמן ציר L90/L110: Volvo Axle Oil 80W-90 GL-5. החלפה כל 2000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "שידור,ציר", "equipment": "L90,L110,L120", "symptom": "בעיות גיר,נסיעה", "brand": "Volvo"}
    },
    {
        "id": "volvo_mini_excavator_ec27_ec55_001",
        "text": (
            "מיני-מחפרון וולוו EC27 ו-EC55 - תקלות נפוצות ותחזוקה\n\n"
            "מאפיינים:\n"
            "- EC27C: משקל 2.7 טון, מנוע 17.5 כ\"ס (Yanmar), עומק חפירה 3.0 מטר\n"
            "- EC55D: משקל 5.5 טון, מנוע 40 כ\"ס (Volvo D1.8), עומק חפירה 4.1 מטר\n\n"
            "1. מנוע EC27 עולה ונכבה (Stalling)\n"
            "   גורם: מסנן דלק סתום — מסנן זעיר ב-EC27 נסתם מהר.\n"
            "   פתרון: החלף מסנן דלק כל 250 שעות (לא 500 כמו כלים גדולים).\n\n"
            "2. EC55 - Boom לא מגיע לגובה מלא\n"
            "   גורם: לחץ Relief נמוך בבלוק שסתומים (Control Valve Block).\n"
            "   בדיקה: חבר מד לחץ לנקודת בדיקה Boom Cylinder Port — לחץ צריך להיות 230 בר.\n"
            "   פתרון: כוון Relief Valve של Boom.\n\n"
            "3. EC27 - סיבוב (Swing) לא עובד\n"
            "   גורם: Swing Motor קטן (Orbital Motor) — רגיש לשמן מלוכלך.\n"
            "   פתרון: החלף שמן הידראולי, נקה פילטר Return Line.\n\n"
            "תחזוקה מיוחדת למיני-מחפרונים:\n"
            "- שמן מנוע: כל 250 שעות (לא 500)\n"
            "- Rubber Track Tension: בדוק כל 50 שעות. מתח נכון: 30-40 ממ רפיון\n"
            "- Final Drive Oil: כל 1000 שעות — SAE 80W-90"
        ),
        "metadata": {"source": "seed", "topic": "מיני-מחפרון", "equipment": "EC27,EC55", "symptom": "תקלות מיני-מחפרון", "brand": "Volvo"}
    },
    {
        "id": "volvo_paver_p5320_p6820_001",
        "text": (
            "מפלסי כביש וולוו P5320/P6820 - תקלות מערכת פיזור\n\n"
            "מפלסי הכביש (Paver) P5320 ו-P6820 של וולוו משמשים לסלילת כביש אספלט.\n"
            "מאפייני P6820: רוחב סלילה: 2.55-8.0 מטר. מנוע: Volvo D6 — 129 כ\"ס.\n\n"
            "1. Screed (לוח פיזור) לא מתחמם\n"
            "   תסמין: אספלט לא נמרח אחיד, פני שטח מחוספסים.\n"
            "   בדיקה: מדוד התנגדות (Resistance) של כל Electric Heating Element — חוט שרוף = אינסוף אוהם.\n"
            "   ערך תקין: ~8–15 אוהם.\n"
            "   קוד VCADS: MID 253 SPN 5246 FMI 3 = מעגל פתוח בלוח חימום.\n\n"
            "2. Auger עוצר בעבודה\n"
            "   גורם: עומס יתר כאשר ערמת אספלט גבוהה מדי, או Auger Motor Pressure Relief נמוך.\n"
            "   בדיקה: לחץ על Auger צריך להיות 250-280 בר.\n"
            "   פתרון: כוון Relief Valve, וודא הזנה אחידה מהמשאית.\n\n"
            "3. Conveyor רץ מצד אחד בלבד\n"
            "   גורם: שסתום כיוונון הידראולי (Flow Control Valve) לקונבייר פגום.\n"
            "   פתרון: החלף Flow Control Valve, בדוק Conveyor Motor לדליפות.\n\n"
            "4. Screed לא מגיע לגובה אחיד (Crown Control)\n"
            "   גורם: Slope Sensor כלול במערכת Niveltronic Plus פגום.\n"
            "   קוד: MID 253 SPN 1079 FMI 2 = Slope Sensor Signal Erratic.\n"
            "   פתרון: כייל מחדש דרך VCADS, אם לא עוזר — החלף חיישן."
        ),
        "metadata": {"source": "seed", "topic": "מפלס כביש,Screed", "equipment": "P5320,P6820", "symptom": "בעיות פיזור אספלט", "brand": "Volvo"}
    },
    {
        "id": "volvo_compactor_sd110_dd120_001",
        "text": (
            "מדחסי וולוו SD110 ו-DD120 - תקלות רטט ומנגנון כביש\n\n"
            "SD110 (מדחס יחיד) ו-DD120 (מדחס כפול).\n"
            "מאפייני DD120: משקל 12 טון, כוח רטט 250 kN, תדר רטט 28-35 Hz, מנוע Volvo D4 — 95 כ\"ס.\n\n"
            "1. ללא רטט (No Vibration) ב-SD110\n"
            "   גורמים:\n"
            "   - Eccentric Shaft פגום.\n"
            "   - מוטור הרטט (Vibration Motor) לא מסתובב — בדוק לחץ הידראולי: צריך 280 בר.\n"
            "   - Vibration Valve (שסתום רטט) תקוע סגור.\n"
            "   קוד VCADS: MID 141 SPN 5017 FMI 7 = Vibration Motor Speed Low.\n\n"
            "2. DD120 רוטט חזק מדי בתדר גבוה\n"
            "   גורם: Amplitude נמוך לא נבחר נכון עבור שטח רגיש.\n"
            "   פתרון: עבור ל-Low Amplitude Mode על הלוח.\n\n"
            "3. הכלי לא נוסע (Travel Failure)\n"
            "   גורם: Hydrostatic Drive Pump (משאבת HST) פגומה או Charge Pressure נמוך.\n"
            "   בדיקה: Charge Pressure צריך להיות 24-28 בר.\n"
            "   פתרון: בדוק Charge Pump, פילטר HST, בדוק דליפות בצינורות High Pressure.\n\n"
            "4. מד דחיסה (CMV) לא מדויק\n"
            "   גורם: Accelerometer (חיישן תאוצה) ב-Drum מלוכלך או רופף.\n"
            "   פתרון: נקה Accelerometer, הדק ברגים, כייל מחדש."
        ),
        "metadata": {"source": "seed", "topic": "מדחס,רטט", "equipment": "SD110,DD120", "symptom": "תקלות רטט,נסיעה", "brand": "Volvo"}
    },
    {
        "id": "volvo_compact_loader_mct85_001",
        "text": (
            "מעמיס קומפקטי וולוו MCT85 (Compact Track Loader) - תקלות ותחזוקה\n\n"
            "מאפיינים: משקל 4,960 ק\"ג, הספק הרמה 1,065 ק\"ג, מנוע Volvo D2.6 Tier 4 Final — 74 כ\"ס.\n\n"
            "1. MCT85 לא נוסע לאחד הצדדים\n"
            "   גורם: Hydrostatic Pump (HST Pump) או Motor פגום לצד אחד.\n"
            "   בדיקה: בדוק Charge Pressure — צריך להיות 26-30 בר.\n"
            "   קוד: MID 253 SPN 1716 FMI 4 = Left Drive Motor Pressure Low.\n\n"
            "2. זרוע הרמה (Lift Arm) לא עולה עד לגובה מלא\n"
            "   גורם: Lift Arm Cylinder Seals שחוקים, או Relief Valve Lift Circuit נמוך.\n"
            "   בדיקה: לחץ צריך להיות 230 בר.\n"
            "   פתרון: החלף חותמות גלינדר (Cylinder Seal Kit).\n\n"
            "3. מלחציים (Attachment) לא מגיבים\n"
            "   קוד: MID 253 SPN 3720 FMI 5 = Auxiliary Solenoid Open Circuit.\n"
            "   פתרון: בדוק חיבורי חוט לסולנואיד, החלף Solenoid אם פגום.\n\n"
            "4. רצועת גומי (Rubber Track) נופלת\n"
            "   בדיקה: מתח נכון — 30 ממ שקיעה בנקודת אמצע הרצועה.\n"
            "   פתרון: מלא גריז ל-Track Adjuster Grease Fitting עד למתח הנכון.\n\n"
            "תחזוקה MCT85:\n"
            "- שמן מנוע: D2.6 — כל 250 שעות\n"
            "- פילטר הידראולי: כל 500 שעות\n"
            "- Chain Case Oil (לכל צד): SAE 30 — כל 1000 שעות"
        ),
        "metadata": {"source": "seed", "topic": "מעמיס קומפקטי,HST", "equipment": "MCT85", "symptom": "בעיות נסיעה,רמה,אביזרים", "brand": "Volvo"}
    },
    {
        "id": "volvo_can_bus_electrical_001",
        "text": (
            "תקשורת CAN Bus ובקרים אלקטרוניים - וולוו EC/L Series\n\n"
            "מכשירי וולוו משתמשים ברשת CAN Bus לתקשורת בין בקרים. רשת ה-CAN פועלת ב-250kbps או 500kbps.\n\n"
            "בקרים ראשיים ב-EC350E:\n"
            "- ECU (MID 140) = בקר מנוע\n"
            "- HCU (MID 141) = בקר הידראוליקה\n"
            "- MCU (MID 253) = בקר מכונה (HMI)\n"
            "- ICU (MID 163) = בקר מכשירים\n\n"
            "1. קודים מרובים בו-זמנית (Multiple Fault Codes)\n"
            "   גורם: תקלת CAN Bus ולא כשל בכל הרכיבים יחד.\n"
            "   אבחון:\n"
            "   - בדוק מתח סוללה: חייב להיות 24V–27V בזמן הפעלה.\n"
            "   - בדוק נתיכים (Fuses) של ה-CAN Bus — לרוב F5 ו-F7 בקופסת נתיכים ראשית.\n"
            "   - בדוק עמידות (Termination Resistors) — צריך להיות 60 אוהם בין CAN-H ל-CAN-L.\n\n"
            "2. BUS OFF — בקר מנותק מהרשת\n"
            "   קוד: MID 140 SID 231 FMI 12 = CAN Bus Communication Failure.\n"
            "   גורם: קצר (Short Circuit) בקו CAN, בקר ECU פגום.\n"
            "   פתרון: בדוק כבל CAN לנזק פיזי, בדוק חיבורים לקורוזיה.\n\n"
            "3. מסך HMI (צג מפעיל) כבוי\n"
            "   גורם: MCU לא מקבל חשמל, או כבל ECU-HMI פגום.\n"
            "   בדיקה: וודא נתיך MCU (בדרך כלל F12 15A).\n\n"
            "עצה לשטח: אם אחרי ניתוק/חיבור סוללה הקודים נעלמים — זה אינדיקציה לבעיה זמנית ב-CAN."
        ),
        "metadata": {"source": "seed", "topic": "CAN Bus,חשמל,בקרים", "equipment": "EC300,EC350,EC380,L90,L110", "symptom": "קודי שגיאה מרובים,תקשורת", "brand": "Volvo"}
    },
    {
        "id": "volvo_excavator_swing_travel_001",
        "text": (
            "מנגנון סיבוב ונסיעה - וולוו EC350/EC380\n\n"
            "סיבוב EC350/EC380:\n"
            "- מנוע הידראולי סיבוב (Swing Motor): Piston Type — לחץ מקסימום 280 בר\n"
            "- גיר סיבוב (Swing Reduction Gear Box): יחס הפחתה 1:17\n"
            "- שמן גיר סיבוב: GL-4 80W בנפח 2.8 ליטר — החלפה כל 2000 שעות\n"
            "- Swing Bearing: שימון כל 500 שעות עם גריז Volvo Extreme Pressure\n\n"
            "1. סיבוב חד-כיווני (Swing Only One Direction)\n"
            "   קוד: MID 141 SPN 5021 FMI 7 = Swing Motor Speed Abnormal.\n"
            "   פתרון: פרק ובדוק Counter-Balance Valve, החלף אם ניכרת שחיקה.\n\n"
            "2. Swing Brake לא משתחרר\n"
            "   בדיקה: בדוק מתח ב-Solenoid — צריך 24V.\n"
            "   קוד: MID 253 SPN 5025 FMI 5 = Swing Brake Solenoid Open.\n\n"
            "נסיעה EC350:\n"
            "- Travel Motor: Piston Type, לחץ מקסימום 420 בר\n"
            "- Final Drive: 2-Speed (Low/High) — Hi-Lo Switch בכבינה\n"
            "- Travel Reduction Gear Box: שמן SAE 90 — 3.5 ליטר לצד — החלפה כל 2000 שעות\n\n"
            "3. כלי נוסע לצד אחד (Pulling To One Side)\n"
            "   קוד: MID 141 SPN 5032 FMI 1 = Right Travel Motor Speed Low.\n\n"
            "4. 2-Speed (Hi) לא עובד\n"
            "   גורם: Travel 2-Speed Solenoid פגום, או לחץ Pilot לא מספיק.\n"
            "   בדיקה: לחץ Pilot בהפעלת Hi צריך להיות 35 בר.\n"
            "   פתרון: החלף 2-Speed Solenoid Valve."
        ),
        "metadata": {"source": "seed", "topic": "סיבוב,נסיעה", "equipment": "EC350,EC380", "symptom": "בעיות סיבוב,נסיעה", "brand": "Volvo"}
    },
    {
        "id": "volvo_fault_codes_mid_fmi_001",
        "text": (
            "מדריך קודי שגיאה - MID/FMI/SPN למכשירי וולוו\n\n"
            "MID 140 - בקר מנוע:\n"
            "- MID 140 SPN 100 FMI 1 = לחץ שמן מנוע נמוך. פעולה: כבה מנוע מיד, בדוק מפלס שמן.\n"
            "- MID 140 SPN 110 FMI 0 = טמפרטורת קירור גבוהה. פעולה: כבה מנוע, בדוק קירור.\n"
            "- MID 140 SPN 190 FMI 8 = אות חיישן RPM לא תקין. פעולה: בדוק חיישן מהירות סיבוב (CKP Sensor).\n"
            "- MID 140 SPN 641 FMI 5 = VGT (Turbo Variable Geometry) מעגל פתוח.\n"
            "- MID 140 SPN 1761 FMI 1 = מפלס AdBlue נמוך.\n"
            "- MID 140 SPN 3251 FMI 0 = לחץ דיפרנציאלי DPF גבוה — נדרשת רגנרציה.\n\n"
            "MID 141 - בקר הידראוליקה:\n"
            "- MID 141 SPN 3508 FMI 0 = שמן הידראולי חם. פעולה: הפחת עומס.\n"
            "- MID 141 SPN 5017 FMI 1 = מהירות נמוכה ב-Vibration Motor.\n"
            "- MID 141 SPN 1246 FMI 3 = חיישן לחץ Pump — מתח גבוה (Short to Power).\n\n"
            "MID 253 - בקר מכונה:\n"
            "- MID 253 SPN 5025 FMI 5 = Swing Brake Solenoid — מעגל פתוח.\n"
            "- MID 253 SPN 3720 FMI 5 = Auxiliary Solenoid — מעגל פתוח.\n"
            "- MID 253 SPN 1421 FMI 12 = Differential Lock — רכיב פגום.\n\n"
            "FMI נפוצים: 0=גבוה, 1=נמוך, 2=לא תקין, 3=קצר לחיובי, 4=קצר לאדמה, "
            "5=מעגל פתוח, 7=כשל מכני, 12=רכיב פגום.\n\n"
            "הערה: SPN 168 FMI 1 (מתח סוללה נמוך) — הסיבה הנפוצה ביותר לקודי שגיאה מרובים."
        ),
        "metadata": {"source": "seed", "topic": "קודי שגיאה,MID,FMI,SPN", "equipment": "EC300,EC350,EC380,L90,L110,P5320,SD110,MCT85", "symptom": "קודי שגיאה", "brand": "Volvo"}
    },
    {
        "id": "volvo_maintenance_schedule_ec350_001",
        "text": (
            "לוח תחזוקה מחפרון וולוו EC350E - לפי שעות\n\n"
            "תחזוקה יומית (Daily) — לפני כל משמרת:\n"
            "- בדוק מפלס שמן מנוע — מוט הבדיקה בין MIN ל-MAX\n"
            "- בדוק מפלס קירור — מיכל הרחבה\n"
            "- בדוק מפלס שמן הידראולי — Sight Glass מצד ימין\n"
            "- בדוק Water Separator — פרוק מים\n"
            "- בדוק מסנן אוויר — אינדיקטור אדום = החלף\n"
            "- שמן נקבי גריז: Boom Foot Pin, Boom Cylinder Pins, Arm Pins, Bucket Pins\n\n"
            "כל 250 שעות:\n"
            "- החלף שמן מנוע (Volvo VDS-4.5 15W-40) + פילטר שמן\n"
            "- החלף מסנן דלק ראשי + Pre-Filter\n"
            "- שמן Swing Bearing דרך Grease Fitting\n\n"
            "כל 500 שעות:\n"
            "- החלף פילטר הידראולי Return Line\n"
            "- החלף פילטר Pilot\n"
            "- בדוק Turbocharger — שמן ורפיון\n\n"
            "כל 1000 שעות:\n"
            "- בדוק Swing Gear Box Oil — החלף אם שחור\n"
            "- בדוק Track Shoes — שחיקה ממרכז השן\n"
            "- בדוק Final Drive Oil לכל צד\n\n"
            "כל 2000 שעות:\n"
            "- החלף שמן הידראולי (Volvo Hydraulic Oil VG46)\n"
            "- החלף שמן Swing Gear Box\n"
            "- החלף שמן Final Drive\n"
            "- בדוק Swing Bearing לרפיון — מקסימום 3 ממ רפיון"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "EC350", "symptom": "תחזוקה", "brand": "Volvo"}
    },
    {
        "id": "volvo_ec300_hydraulic_pump_fault_001",
        "text": (
            "תקלות משאבה הידראולית - וולוו EC300/EC350/EC380\n\n"
            "המשאבה ההידראולית (Main Hydraulic Pump) בסדרת EC300-EC380 היא משאבת פיסטון כפולה "
            "(Tandem Piston Pump) מסוג Kawasaki K3VL.\n\n"
            "ספציפיקציות:\n"
            "- ספיקה מקסימום: 2 x 205 ליטר לדקה (EC380E)\n"
            "- לחץ שיא: 380 בר. לחץ עבודה: 350 בר\n"
            "- מנגנון: Load Sensing + Pressure Compensation\n\n"
            "אבחון משאבה עם VCADS Pro:\n"
            "1. כנס ל-MID 141, קרא Main Pump 1 Pressure ו-Main Pump 2 Pressure בזמן אמת.\n"
            "2. בעומס מלא: הלחץ צריך להגיע ל-340-350 בר.\n"
            "3. אם אחד מהם מראה פחות מ-280 בר בעומס — בעיה בחלק הספציפי.\n\n"
            "1. ספיקה נמוכה (Low Flow) — זרועות איטיות\n"
            "   גורם: בלאי פיסטונים (Pistons) ב-Cylinder Block.\n"
            "   ירידה של 20% מהנורמלי = משאבה בסוף חיים.\n\n"
            "2. Cutoff Valve לא מגיב\n"
            "   קוד: MID 141 SPN 1246 FMI 4.\n"
            "   פתרון: החלף Regulator Solenoid.\n\n"
            "3. קאוויטציה חזקה (Cavitation Noise)\n"
            "   גורם: Suction Filter סתום, שמן נמוך, שמן קר מדי.\n"
            "   פתרון: נקה Suction Filter. הרץ מנוע 5 דקות ב-Low Idle לפני עבודה בקור.\n\n"
            "4. דליפה חיצונית ממשאבה\n"
            "   מיקום שכיח: Shaft Seal (אטם ציר המשאבה).\n"
            "   פתרון: החלף Shaft Seal Kit — עבודה של 4 שעות.\n"
            "   שמן: אם משאבה מאבדת יותר מ-100cc לשעה = החלפה דחופה."
        ),
        "metadata": {"source": "seed", "topic": "משאבה הידראולית", "equipment": "EC300,EC350,EC380", "symptom": "ספיקה נמוכה,קאוויטציה,דליפה", "brand": "Volvo"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Volvo entries. Total KB: {rag.count()} chunks")
