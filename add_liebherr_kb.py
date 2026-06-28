"""Add Liebherr knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "liebherr_excavator_hydraulic_r920_r926_001",
        "text": (
            "ליבהר R920 / R926 / R936 - תקלות הידראוליקה ואובדן לחץ\n\n"
            "מחפרוני ליבהר סדרת R9 מצוידים במערכת Positive Control Hydraulics עם משאבות פיסטון כפולות.\n\n"
            "1. אובדן כוח הידראולי כללי (General Hydraulic Power Loss)\n"
            "   ספציפיקציות: לחץ מערכת R926 = 350 בר, Pilot Pressure = 40 בר.\n"
            "   בדיקה ראשונה: חבר מד לחץ לנקודת בדיקה MP1/MP2 ליד גוש השסתומים הראשי.\n"
            "   גורם נפוץ: רגולטור המשאבה (Pump Regulator) — בדוק פתח הכוונה בפיזי.\n"
            "   כלי אבחון: LiDat (Liebherr Data System) — קרא Plant Parameter 'Pump Pressure 1'.\n\n"
            "2. בלוק שסתומים ראשי (Main Control Valve) תקוע\n"
            "   ליבהר R926 עם MCV electorhydraulic — השסתומים נשלטים ב-Pilot pressure.\n"
            "   גורם: אבק/זיהום שמן תוקע Spool.\n"
            "   פתרון: הוסף מגנט Drain Line, נקה פילטר Return בכל 250 שעות, החלף שמן הידראולי.\n\n"
            "3. קאוויטציה במשאבה (Pump Cavitation)\n"
            "   תסמין: רעש 'לחיצה' בהזנקה, במיוחד בקור.\n"
            "   גורם: Suction Strainer סתום, ויסקוזיטה שמן גבוהה בקור.\n"
            "   שמן מאושר ליבהר: Liebherr Hydraulic Oil HEES 46 או שמן מינרלי HLP 46.\n"
            "   פתרון: הרץ Low Idle 5 דקות לפני עומס מלא בטמפרטורות נמוכות.\n\n"
            "4. Arm/Boom איטיים בצד שמאל בלבד\n"
            "   גורם: Load Check Valve תקוע בגוש שסתומים ימין.\n"
            "   R926 עם שני MCV נפרדים (ימין ושמאל).\n"
            "   פתרון: פרק ה-MCV הרלוונטי, נקה Check Ball + Spring, החלף O-rings."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "R920,R926,R936", "symptom": "אובדן לחץ הידראולי", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_excavator_engine_r926_r950_002",
        "text": (
            "ליבהר R926 / R950 - מנועי Liebherr D934 / D946 ותקלות מנוע\n\n"
            "ליבהר מייצרת מנועים עצמאית — סדרת D934 (6 צילינדרים, 9 ליטר) ו-D946 (6 צילינדרים, 12 ליטר).\n\n"
            "מאפייני מנוע D934 ב-R926:\n"
            "- הספק: 190 כ\"ס (140 קוט\"ש)\n"
            "- מומנט: 980 ניוטון-מטר\n"
            "- Common Rail Injection, Stage V / Tier 4 Final\n\n"
            "1. עשן שחור + חוסר כוח\n"
            "   גורם א: Turbocharger VTG תקוע — Vanes לא נעות.\n"
            "   בדיקה: LiDat → Engine Parameters → Turbo Boost Pressure.\n"
            "   לחץ תקין בעומס: 200–230 kPa.\n"
            "   פתרון: נקה VTG Actuator ו-Vanes בתרסיס מנקה, בדוק Actuator Rod.\n\n"
            "2. DEF/AdBlue Fault (SCR System)\n"
            "   קוד LiDat: Engine ECU → DTC P20EE = Reducing Agent Quality.\n"
            "   פתרון: נקז מיכל DEF, שטוף, מלא ISO 22241-1. בדוק DEF Quality Sensor.\n\n"
            "3. DPF Regeneration לא מצליח\n"
            "   קוד: DTC P2453 = DPF Differential Pressure High.\n"
            "   פתרון: בצע Stationary Regen דרך LiDat → Service → DPF Regeneration.\n"
            "   אם נכשל 3 פעמים — יש להוציא DPF לניקוי מקצועי (Thermal Cleaning).\n\n"
            "4. קירור יתר בקור (Engine Not Reaching Temperature)\n"
            "   גורם: Thermostat תקוע פתוח.\n"
            "   טמפרטורת מנוע תקינה: 80–95°C.\n"
            "   פתרון: החלף Thermostat — מאוד נפוץ בישראל בחורף.\n\n"
            "5. רעש 'נקישה' מהמנוע בהזנקה\n"
            "   גורם: Hydraulic Tappets (דפדפות הידראוליות) לא מתמלאות.\n"
            "   פתרון: החלף שמן מנוע Liebherr SAE 15W-40 ACEA E9, הפעל Low Idle 2 דק' לפני עומס."
        ),
        "metadata": {"source": "seed", "topic": "מנוע D934,D946", "equipment": "R926,R950", "symptom": "חוסר כוח,עשן שחור,DPF", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_crane_ltm1100_003",
        "text": (
            "ליבהר LTM 1100-5.2 עגורן נייד - תקלות מערכת הרמה והגדרת עומס\n\n"
            "ה-LTM 1100-5.2 הוא עגורן נייד (Mobile Crane) בעל יכולת הרמה של 100 טון, זרוע טלסקופית 60 מטר.\n\n"
            "1. LICCON מחשב שגיאת עומס (Load Limit Exceeded)\n"
            "   LICCON (Liebherr Computer CONtrol) הוא מחשב הגנת העומס הראשי.\n"
            "   קוד: E1001 = גלאי עומס (Load Moment Indicator) עולה על 100%.\n"
            "   פעולה חובה: הנח עומס מיד! בדוק טבלת עומסים (Load Chart) לתנאי השמיש.\n"
            "   גורם נפוץ: רדיוס עבודה (Outreach) גדול מהמוגדר בתצורה.\n\n"
            "2. LICCON קוד E2100 - כשל מדידת זווית הזרוע (Boom Angle Sensor Fault)\n"
            "   גורם: חיישן זווית (Angle Sensor) מלוכלך/פגום בבסיס הזרוע.\n"
            "   בדיקה: LICCON → Service Mode → Calibration → Boom Angle.\n"
            "   פתרון: נקה חיישן, כייל מחדש. אם שגוי — החלף Sensor HA2.\n\n"
            "3. הזרוע הטלסקופית לא מתארכת (Boom Extension Failure)\n"
            "   גורם א: לחץ הידראולי נמוך לגלינדר הטלסקופי (< 280 בר).\n"
            "   גורם ב: כבל סינכרון (Synchronization Cable) קרוע.\n"
            "   בדיקה: פרק כיסוי צד Boom, בדוק מצב הכבל ועקרות Sheaves.\n\n"
            "4. רגלי תמיכה (Outriggers) לא נפרסים\n"
            "   גורם: שסתום הידראולי של Outrigger תקוע, או חיישן גבול (Limit Switch) פגום.\n"
            "   LTM 1100 עם בקרת Outrigger LICCON — בדוק LED סטטוס כל רגל.\n"
            "   בדיקה: LICCON → Outrigger Control → Status Display.\n\n"
            "5. קוד LICCON E5000 - כשל תקשורת CAN\n"
            "   בדוק חיבורי CAN Bus בלוח החשמל הראשי (Main Electrical Cabinet).\n"
            "   בדיקת עמידות: 60 אוהם בין CAN-H ל-CAN-L."
        ),
        "metadata": {"source": "seed", "topic": "עגורן נייד,LICCON", "equipment": "LTM1100,LTM1060,LTM1080", "symptom": "שגיאת עומס,זרוע לא מתארכת", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_wheel_loader_l538_l542_004",
        "text": (
            "ליבהר L538 / L542 / L550 מטענים גלגלים - תקלות שידור וזרועות\n\n"
            "מטעיני הגלגלים L538/L542 של ליבהר מצוידים בתיבת הילוכים הידרוסטטית (Hydrostatic Transmission)\n"
            "ומנוע Liebherr D934 בהספק 120–145 כ\"ס.\n\n"
            "1. מהירות נסיעה מוגבלת (Reduced Travel Speed)\n"
            "   מטעיני ליבהר עם HST (Hydrostatic Transmission) — הנעה ישירה דרך Hydrostatic Pump + Motor.\n"
            "   גורם: Charge Pressure נמוך מתחת ל-22 בר.\n"
            "   בדיקה: פורט בדיקה Charge Pressure ליד ה-HST Pump.\n"
            "   פתרון: בדוק Charge Filter, צינור Suction, אטמי Charge Pump.\n\n"
            "2. מטען לא עולה בעומס מלא\n"
            "   L542: לחץ Relief לעליית הזרוע = 260 בר.\n"
            "   גורם: Relief Valve Lift Cylinder לא מכוון נכון.\n"
            "   כוון בברגי כיוון (Adjustment Screw) ב-MCV — עלייה של 20 בר לכל סיבוב מלא.\n\n"
            "3. Kickdown לא עובד\n"
            "   ליבהר L538/L542 עם מתג Kickdown על דוושת Gas — עובר ל-Torque Converter Mode בלחיצה.\n"
            "   גורם: מתג Kickdown פגום, או פרמטר TCU לא מוגדר.\n"
            "   בדיקה: LiDat → Transmission → Kickdown Switch Status.\n\n"
            "4. 'ניתוק' פתאומי בנסיעה (Sudden Loss of Drive)\n"
            "   גורם: חיישן טמפרטורת שמן HST עולה מעל 105°C — System Cutout.\n"
            "   פתרון: הפסק עבודה, קרר מנוע, בדוק מקרר שמן HST (Oil Cooler).\n\n"
            "5. רעש 'נקישה' מגשר הקדמי\n"
            "   גורם: בלאי Cross Pin ב-Differential.\n"
            "   שמן גשר: Liebherr Axle Oil SAE 90 GL-5.\n"
            "   בדוק מפלס שמן ב-Drain Plug — החלף כל 2000 שעות."
        ),
        "metadata": {"source": "seed", "topic": "מטען גלגלים,HST", "equipment": "L538,L542,L550", "symptom": "מהירות מוגבלת,זרוע לא עולה", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_lidat_diagnostic_005",
        "text": (
            "מערכת אבחון LiDat וLiDAT Web - ליבהר\n\n"
            "LiDat (Liebherr Data Transmission System) היא מערכת הטלמטיקה והאבחון של ליבהר.\n"
            "LiDAT Web מאפשר מעקב מרחוק על מצב הכלי, שעות עבודה וקודי שגיאה.\n\n"
            "חיבור מקומי:\n"
            "1. חבר ממשק USB-to-CAN (Liebherr Service Adapter) לשקע Deutsch 9-pin.\n"
            "2. פתח תוכנת LiDat Service Tool.\n"
            "3. בחר Machine Type ו-Serial Number.\n"
            "4. גש ל-Diagnostic → Fault Codes.\n\n"
            "קטגוריות קודי שגיאה (DTC) נפוצים:\n"
            "- Engine ECU: P0087 = לחץ Rail נמוך, P0401 = EGR Low Flow\n"
            "- Hydraulic ECU: H0001 = לחץ מערכת נמוך, H0042 = טמפרטורת שמן גבוהה\n"
            "- Transmission ECU: T0011 = Clutch Slip, T0021 = Shift Error\n"
            "- Machine ECU: M0031 = Joystick Fault, M0055 = CAN Timeout\n\n"
            "Active Tests דרך LiDat:\n"
            "- הפעל/כבה כל סולנואיד בנפרד לאבחון\n"
            "- קרא ערכי חיישנים בזמן אמת (Live Data)\n"
            "- בצע כיולי חיישנים (Calibration)\n"
            "- אפס קודי שגיאה לאחר תיקון\n\n"
            "מה לעשות עם קודי שגיאה מרובים בו-זמנית:\n"
            "1. בדוק מתח סוללה — חייב להיות 24V–27.5V.\n"
            "2. בדוק SPN 168 (Battery Voltage) — כל קוד שנגרם ממתח נמוך ייעלם לאחר טעינת סוללה.\n"
            "3. קרא ה-Freeze Frame Data — מה היה מצב הכלי בזמן השגיאה."
        ),
        "metadata": {"source": "seed", "topic": "אבחון LiDat", "equipment": "R920,R926,R950,L538,L542,LTM1100", "symptom": "קודי שגיאה,אבחון כללי", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_excavator_track_swing_r936_006",
        "text": (
            "ליבהר R936 - מערכת נסיעה, זחלים וסיבוב\n\n"
            "1. Final Drive Oil Leak (דליפת שמן Drive הסופי)\n"
            "   R936 עם Float Seal על כל Final Drive.\n"
            "   נפח שמן: SAE 80W-90 GL-4 — 5.5 ליטר לצד.\n"
            "   תסמין: שמן כהה על Sprocket ואזור זחל.\n"
            "   פתרון: החלף Float Seal — פרק Sprocket, נקה, החלף O-rings + Seal.\n\n"
            "2. Travel לצד אחד בלבד\n"
            "   גורם: Anti-Cavitation Valve בצד אחד פגום, גורם ל-Cavitation ב-Motor.\n"
            "   בדיקה: לחץ High Pressure ב-Travel Motor — צריך 380–420 בר בעומס.\n"
            "   פתרון: החלף Anti-Cavitation Check Valve.\n\n"
            "3. Swing Bearing שחוק (Swing Ring Gear Wear)\n"
            "   R936: בדוק רפיון אנכי כל 1000 שעות עם Dial Gauge.\n"
            "   מקסימום מותר: 2.5 מ\"מ.\n"
            "   שימון: כל 250 שעות, 8 נקבי גריז — גריז Liebherr EP2 (NLGI 2).\n\n"
            "4. Swing (סיבוב) איטי\n"
            "   R936: לחץ Swing Motor = 280 בר.\n"
            "   גורם: Swing Relief Valve לא מכוון נכון — כוון לפי LiDat H0015.\n"
            "   תסמין נוסף: אם סיבוב 'קופץ' — בדוק Swing Brake Valve."
        ),
        "metadata": {"source": "seed", "topic": "זחלים,סיבוב,נסיעה", "equipment": "R936,R926", "symptom": "דליפת שמן Drive,נסיעה חד-צדדית,סיבוב איטי", "brand": "Liebherr"}
    },
    {
        "id": "liebherr_maintenance_schedule_007",
        "text": (
            "לוח תחזוקה מחפרון ליבהר R926 - לפי שעות עבודה\n\n"
            "תחזוקה יומית — לפני משמרת:\n"
            "- בדוק מפלס שמן מנוע D934 (בין MIN ל-MAX)\n"
            "- בדוק נוזל קירור (בין COLD ל-HOT)\n"
            "- בדוק מפלס שמן הידראולי — Sight Glass בצד ימין של המיכל\n"
            "- בדוק Water Separator (מיכל שקוף על מסנן הדלק)\n"
            "- שמן נקבי גריז: 10 נקבים ב-Boom, Arm, Bucket — גריז EP2\n\n"
            "כל 250 שעות:\n"
            "- החלף שמן מנוע + פילטר (Liebherr SAE 15W-40 ACEA E9, 20 ליטר)\n"
            "- החלף מסנן דלק ראשי ומשני\n"
            "- שמן Swing Bearing — 8 נקבים\n"
            "- בדוק רמת שמן Final Drive שני הצדדים\n\n"
            "כל 500 שעות:\n"
            "- החלף פילטר Return Line הידראולי\n"
            "- החלף פילטר Pilot\n"
            "- בדוק תיפקוד LICCON / LiDat — קרא קודי שגיאה\n"
            "- בדוק Track Tension — רפיון 20-30 מ\"מ בין Idler ל-Carrier Roller\n\n"
            "כל 1000 שעות:\n"
            "- החלף שמן Final Drive (SAE 80W-90 GL-4, 5.5 ליטר לצד)\n"
            "- בדוק Swing Bearing לרפיון אנכי\n"
            "- בדוק ובלם Track Shoe Bolts — 340 Nm\n"
            "- בדוק Turbocharger — שמן, רפיון ציר, נזילות\n\n"
            "כל 2000 שעות:\n"
            "- החלף שמן הידראולי מלא (Liebherr HEES 46, 220 ליטר)\n"
            "- בדוק Swing Reduction Gear Oil (GL-4 80W, 2.8 ליטר)\n"
            "- בדוק Cooling System — שטוף וניקוי קורות קירור"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "R926,R936,R920", "symptom": "תחזוקה", "brand": "Liebherr"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Liebherr entries. Total KB: {rag.count()} chunks")
