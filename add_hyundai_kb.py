"""Add Hyundai Construction Equipment knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "hyundai_excavator_hydraulic_r210_r220_001",
        "text": (
            "יונדאי R210LC-9 / R220LC-9 / R250LC-7 - תקלות הידראוליקה\n\n"
            "מחפרוני יונדאי סדרת R-9 מצוידים במשאבת פיסטון כפולה Kawasaki K3V112/K3V140\n"
            "עם מערכת Negative Flow Control (NFC) — דומה לשיטת היטאצ'י.\n\n"
            "1. אובדן כוח הידראולי — כלי איטי\n"
            "   לחץ מערכת R210LC-9: 34.3 MPa (343 בר).\n"
            "   לחץ Pilot: 3.9 MPa (39 בר).\n"
            "   בדיקה: חבר מד לחץ לנקודות G1/G2 (ליד Pump) ול-GP (Pilot).\n"
            "   גורם נפוץ: NFC Relief Valve לא מכוון — לחץ NFC ב-Neutral: 2.9 MPa (29 בר).\n"
            "   פתרון: כוון NFC Relief בגוש שסתומים ראשי (MCV).\n\n"
            "2. Boom / Arm חלשים מצד אחד\n"
            "   גורם: Load Check Valve תקוע ב-MCV.\n"
            "   R210: MCV עם 9 Spool נפרדים — פרק Spool הרלוונטי, נקה, החלף O-rings.\n\n"
            "3. שמן הידראולי מתחמם (Overheating)\n"
            "   R210: גבול אזהרה 95°C, גבול כיבוי 105°C.\n"
            "   גורם: Oil Cooler סתום, מאוורר Cooler לא מסתובב.\n"
            "   בדיקה Hi-Mate: Monitor → Oil Temp Sensor (Port T).\n"
            "   פתרון: נקה Oil Cooler, בדוק Fan Belt, בדוק Thermostat שמן.\n\n"
            "4. Pump Regulator לא שולט בספיקה\n"
            "   R220 עם Electronic Pump Control (EPC Solenoid).\n"
            "   קוד Hi-Mate: 0x1101 = EPC Solenoid Current Out of Range.\n"
            "   בדיקה: מדוד התנגדות EPC Solenoid — תקין: 5–7 אוהם.\n"
            "   פתרון: החלף EPC Solenoid, בדוק Harness לנזק."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,NFC", "equipment": "R210LC-9,R220LC-9,R250LC-7", "symptom": "כלי איטי,שמן חם,לחץ נמוך", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_himate_diagnostic_002",
        "text": (
            "מערכת אבחון Hi-Mate (Hyundai Intelligent Management & Assist Tool Engineering)\n\n"
            "Hi-Mate היא תוכנת האבחון הרשמית של יונדאי לציוד בנייה (מחפרונים, טעונים).\n"
            "גרסה עדכנית: Hi-Mate v2.x — פועלת על Windows.\n"
            "חיבור: ממשק USB→CAN (Hyundai Service Adapter, Deutsch 9-pin).\n\n"
            "בקרים עיקריים שניתן לגשת אליהם:\n"
            "- ECM (Engine Control Module): קודי מנוע Cummins / Hyundai\n"
            "- HCU (Hydraulic Control Unit): שסתומים, לחצים\n"
            "- MCU (Machine Control Unit): שליטה כללית, Joystick\n"
            "- ICF (Instrument Cluster): מסך, חיישנים\n\n"
            "קודי שגיאה נפוצים (DTC):\n"
            "- 0x0101: Engine Oil Pressure Low — כבה מנוע מיד!\n"
            "- 0x0201: Engine Coolant Temperature High\n"
            "- 0x0301: Hydraulic Oil Temperature High\n"
            "- 0x0401: Battery Voltage Low (< 22V)\n"
            "- 0x0501: Pilot Pressure Sensor Fault\n"
            "- 0x1001: Swing Brake Solenoid Open Circuit\n"
            "- 0x1101: EPC Solenoid (Pump Control) Fault\n"
            "- 0x2001: CAN Bus Communication Error\n\n"
            "Active Tests דרך Hi-Mate:\n"
            "- הפעל/כבה כל Solenoid בנפרד\n"
            "- קרא Live Data: לחץ, טמפרטורה, RPM, אות Joystick\n"
            "- בצע Pump Calibration (כיול ספיקת משאבה)\n"
            "- אפס קודי שגיאה לאחר תיקון\n\n"
            "טיפ: קודים מרובים בו-זמנית — בדוק קודם קוד 0x0401 (מתח סוללה נמוך),\n"
            "שכן מתח נמוך גורם לקודים מדומים בכל המערכות."
        ),
        "metadata": {"source": "seed", "topic": "אבחון Hi-Mate", "equipment": "R210LC-9,R220LC-9,R300LC-9,HL760", "symptom": "קודי שגיאה,אבחון", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_engine_cummins_qsb_003",
        "text": (
            "מנועי Cummins QSB6.7 / QSL9 במחפרוני יונדאי - תקלות נפוצות\n\n"
            "יונדאי משתמשת במנועי Cummins בחלק גדול מהמחפרונים:\n"
            "- R210LC-9 / R220LC-9: Cummins QSB6.7 (173 כ\"ס)\n"
            "- R300LC-9 / R320LC-9: Cummins QSL9 (231 כ\"ס)\n"
            "- R380LC-9: Cummins QSM11 (295 כ\"ס)\n\n"
            "1. מנוע לא מגיע ל-RPM מלא (Power Derate)\n"
            "   Cummins QSB6.7 עם SCR + DPF.\n"
            "   גורם א: DEF/AdBlue נמוך — Derate ב-10% ולאחר מכן 25%.\n"
            "   מלא DEF (ISO 22241, 32.5% אוריאה) — אין לדחות!\n"
            "   גורם ב: DPF Soot Level גבוה — נדרש Regen.\n"
            "   קוד Cummins: SPN 3251 FMI 0 = DPF Differential Pressure.\n\n"
            "2. Cummins Insite — אבחון מנוע\n"
            "   Cummins Insite היא תוכנת האבחון של Cummins (נפרדת מ-Hi-Mate).\n"
            "   קודי נפוצים:\n"
            "   - SPN 100 FMI 1 = לחץ שמן מנוע נמוך\n"
            "   - SPN 110 FMI 0 = טמפרטורת קירור גבוהה\n"
            "   - SPN 641 FMI 7 = VGT Actuator Mechanical Fault\n"
            "   - SPN 1761 FMI 1 = DEF Level Low\n"
            "   - SPN 3031 FMI 0 = DEF Temperature High\n\n"
            "3. Cummins QSB6.7 עשן שחור + חוסר כוח\n"
            "   גורם א: VGT (Variable Geometry Turbo) תקוע.\n"
            "   בדיקה Insite: Turbo Boost Pressure בעומס — תקין: 180–220 kPa.\n"
            "   פתרון: Insite → Active Test → VGT Actuator Calibration.\n"
            "   גורם ב: EGR Valve סתום — נקה עם ספריי EGR Cleaner.\n\n"
            "4. מנוע Cummins QSL9 רעש 'חבטה'\n"
            "   גורם: Injector Cup (קערת מזרק) בלוי — נפוץ ב-QSL9 מעל 8,000 שעות.\n"
            "   בדיקה: Insite → Cylinder Cutout Test — זהה מזרק עם Contribution נמוח.\n"
            "   פתרון: פרק ראש, החלף Injector Cups ו-O-rings."
        ),
        "metadata": {"source": "seed", "topic": "מנוע Cummins QSB,QSL", "equipment": "R210LC-9,R220LC-9,R300LC-9,R320LC-9", "symptom": "חוסר כוח,עשן שחור,DPF,DEF", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_excavator_swing_travel_004",
        "text": (
            "יונדאי R220LC-9 / R300LC-9 - מערכת סיבוב (Swing) ונסיעה (Travel)\n\n"
            "סיבוב R220LC-9:\n"
            "- Swing Motor: Kawasaki MAG-170VP\n"
            "- לחץ Swing מקסימום: 28.0 MPa (280 בר)\n"
            "- שמן גיר סיבוב (Swing Reduction Gear): GL-4 80W — 2.6 ליטר\n"
            "- Swing Bearing: שימון כל 250 שעות — גריז EP2 NLGI-2, 8 נקבים\n\n"
            "1. סיבוב 'מתקשה' להתחיל (Swing Slow to Start)\n"
            "   גורם: Swing Parking Brake לא משתחרר מהר.\n"
            "   בדיקה: לחץ Pilot לשחרור Brake: 3.5 MPa (35 בר).\n"
            "   פתרון: בדוק Swing Brake Release Valve, נקה Orifice.\n\n"
            "2. סיבוב 'גולש' (Swing Drift After Stop)\n"
            "   גורם: Swing Motor Anti-Cavitation Valve פגום — שמן עוזב Motor לאחר עצירה.\n"
            "   פתרון: החלף Anti-Cavitation Check Valve ב-Swing Motor.\n\n"
            "3. Swing Bearing חריקה\n"
            "   R220: 8 נקבי גריז — שמן כל 250 שעות בגריז EP2.\n"
            "   אם חריקה לאחר שימון — בדוק רפיון אנכי: מקסימום 3 מ\"מ עם Dial Gauge.\n\n"
            "נסיעה R300LC-9:\n"
            "- Travel Motor: Kawasaki MAG-170, לחץ מקסימום 40 MPa (400 בר)\n"
            "- Final Drive: 2-Speed, שמן SAE 80W-90 GL-4 — 4.0 ליטר לצד\n\n"
            "4. כלי נוסע לצד אחד (Pulling)\n"
            "   גורם: Straight Travel Valve ב-MCV לא מסנכרן את שני Motor.\n"
            "   R300: פרק MCV, בדוק Straight Travel Spool, נקה ושמן.\n\n"
            "5. Final Drive Oil Seal דולף\n"
            "   תסמין: שמן על הזחל מאחורי Sprocket.\n"
            "   פתרון: החלף Float Seal — פרק Hub, נקה, החלף O-ring + Float Seal Kit."
        ),
        "metadata": {"source": "seed", "topic": "סיבוב,נסיעה,זחלים", "equipment": "R220LC-9,R300LC-9,R210LC-9", "symptom": "סיבוב גולש,כלי נוסע לצד,דליפת שמן Drive", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_excavator_electrical_005",
        "text": (
            "יונדאי R210 / R220 / R300 - מערכות חשמל, CAN Bus ולוח בקרה\n\n"
            "מחפרוני יונדאי R-9 עם ארכיטקטורת CAN Bus:\n"
            "- CAN 1 (500 kbps): ECM (מנוע) + HCU (הידראוליקה)\n"
            "- CAN 2 (250 kbps): MCU + ICF (מסך) + Joystick\n\n"
            "1. מסך מוניטור (ICF) לא דולק\n"
            "   גורם א: נתיך F5 (15A) שרוף — קופסת נתיכים בתא נהג, מכסה שמאל.\n"
            "   גורם ב: Connector CN-ICF (16-pin) מאחורי המסך רופף.\n"
            "   בדיקה: מדוד 24V על Pin 1 (Power) ו-Pin 2 (Ground) של Connector.\n\n"
            "2. Joystick EH לא מגיב\n"
            "   R210/R220 מ-2012 עם Joystick חשמלי (Hall Sensor).\n"
            "   קוד Hi-Mate: 0x0901 = Left Joystick X-Axis Fault.\n"
            "   בדיקה: Hi-Mate → Live Data → Joystick Voltage (תקין: 0.5–4.5V).\n"
            "   פתרון: החלף Joystick Assembly (זוג, ימין ושמאל).\n\n"
            "3. Alternator לא טוען\n"
            "   R210/R220: מערכת 24V, Alternator 80A.\n"
            "   מתח תקין במנוע דולק: 27.5–28.5V.\n"
            "   גורם נפוץ: V-Belt (רצועת Alternator) החליקה/נשברה.\n"
            "   בדיקה: Hi-Mate → Battery Voltage Monitor.\n\n"
            "4. קודי CAN Bus מרובים בבת אחת\n"
            "   גורם נפוץ: מתח סוללה נמוך (< 22V) — כל הבקרים מדווחים שגיאה.\n"
            "   בדיקה ראשונה: Hi-Mate → Fault 0x0401 (Battery Voltage).\n"
            "   בדיקה CAN: Termination Resistors בין CAN-H ל-CAN-L — צריך 60 אוהם.\n"
            "   מיקום Resistors: ליד ECM ב-Engine Bay וליד MCU בתא נהג.\n\n"
            "5. מצלמה אחורית לא עובדת\n"
            "   R220/R300: מצלמה אחורית סטנדרטית.\n"
            "   גורם: כבל Coaxial קצר באזור Swing Bearing (מסתובב).\n"
            "   פתרון: בדוק Slip Ring / Rotary Coupler בחלק התחתון של תא."
        ),
        "metadata": {"source": "seed", "topic": "חשמל,CAN Bus,Joystick", "equipment": "R210LC-9,R220LC-9,R300LC-9", "symptom": "מסך כבוי,Joystick לא מגיב,קודי שגיאה מרובים", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_wheel_loader_hl760_hl780_006",
        "text": (
            "יונדאי HL760 / HL780 מטעין גלגלים - תקלות שידור וזרועות\n\n"
            "מטעיני הגלגלים HL760-9 ו-HL780-9 של יונדאי.\n"
            "HL760-9: מנוע Cummins QSB6.7 (181 כ\"ס), עומס הפעלה: 5.3 טון.\n"
            "HL780-9: מנוע Cummins QSL9 (231 כ\"ס), עומס הפעלה: 7.4 טון.\n\n"
            "תיבת הילוכים: ZF 4WG-200 (HL760) / ZF 4WG-260 (HL780) — Powershift אוטומטי.\n\n"
            "1. תיבת גיר לא עוברת לגיר 3 / 4\n"
            "   קוד Hi-Mate: 0x1201 = ZF Transmission Shift Fault.\n"
            "   גורם: Clutch Solenoid שחוק, לחץ Clutch נמוך מ-14 בר.\n"
            "   שמן מאושר: ZF Lifeguard Fluid 6.\n"
            "   בדיקה: חבר מד לחץ ל-Port P ב-ZF — בדוק לחץ Clutch בכל הילוך.\n\n"
            "2. 'בהלה' בין הילוכים בנסיעה (Transmission Hunting)\n"
            "   גורם: Auto-Shift Sensor (מד מהירות גלגל) פגום — גיר לא יודע מתי לחלף.\n"
            "   קוד ZF: Fault E012 = Output Speed Sensor.\n"
            "   פתרון: בדוק חיישן מהירות Output Shaft — נקה/החלף.\n\n"
            "3. זרוע לא עולה בעומס מלא\n"
            "   HL760: לחץ Relief לעליית זרוע = 250 בר.\n"
            "   גורם: Relief Valve Lift Circuit לחץ נמוך.\n"
            "   בדיקה: חבר מד לחץ ל-Boom Cylinder Port A — בדוק בעליית עומס מלא.\n\n"
            "4. Steering כבד בסיבוב (Heavy Steering)\n"
            "   HL760/HL780 עם Hydrostatic Steering (Orbitrol).\n"
            "   גורם: Steering Priority Valve פגום — שמן הולך לזרוע ולא להיגוי.\n"
            "   בדיקה: לחץ היגוי תקין: 175–210 בר.\n"
            "   פתרון: נקה/החלף Steering Priority Valve Spool.\n\n"
            "5. Bucket (כף) לא מגיעה לזווית מלאה\n"
            "   גורם: Tilt Relief Valve נמוך, או Bucket Cylinder Internal Leak.\n"
            "   לחץ Tilt תקין HL760: 250 בר."
        ),
        "metadata": {"source": "seed", "topic": "מטען גלגלים,ZF,שידור", "equipment": "HL760,HL780", "symptom": "בעיות גיר,זרוע לא עולה,היגוי כבד", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_r300_r380_large_excavator_007",
        "text": (
            "יונדאי R300LC-9 / R320LC-9 / R380LC-9 מחפרונים גדולים\n\n"
            "מחפרוני הסדרה הגדולה של יונדאי (30–38 טון) עם מנועי Cummins QSL9/QSM11.\n\n"
            "1. Pump 1 חלשה מ-Pump 2 (Pump Imbalance)\n"
            "   R300/R380 עם 2 משאבות נפרדות.\n"
            "   Pump 1 מפעילה: Boom + Right Travel.\n"
            "   Pump 2 מפעילה: Arm + Swing + Left Travel.\n"
            "   אם Boom + Right Travel איטיים = Pump 1 בעיה.\n"
            "   בדיקה: Hi-Mate → Live Data → Pump 1 vs. Pump 2 Pressure.\n\n"
            "2. Main Relief Valve שחוק\n"
            "   R300: Main Relief מוגדר ל-34.3 MPa (343 בר).\n"
            "   תסמין: לחץ לא עולה מעל 280 בר גם בעומס מלא.\n"
            "   כיוון: בורג כיוון Main Relief ב-MCV — כל סיבוב = כ-20 בר.\n"
            "   אזהרה: לאחר כיוון — תמיד בדוק לחץ עם Gauge לפני עבודה!\n\n"
            "3. Travel Counterbalance Valve — כלי יורד במדרון\n"
            "   R380: Counterbalance Valve מגביל זרימה בירידת מדרון.\n"
            "   תסמין: כלי מאיץ בירידה ללא שליטה.\n"
            "   פתרון: החלף Counterbalance Valve Assembly (זוג — שני הצדדים).\n\n"
            "4. Power Boost לא פועל\n"
            "   R300/R380 עם Power Boost (לחצן על Joystick) — מעלה לחץ ל-37 MPa ל-8 שניות.\n"
            "   קוד Hi-Mate: 0x1102 = Power Boost Solenoid Open Circuit.\n"
            "   בדיקה: מדוד התנגדות Solenoid — תקין: 7–9 אוהם.\n"
            "   פתרון: החלף Power Boost Solenoid.\n\n"
            "5. Boom Cylinder Internal Seal Leak\n"
            "   R380: גלינדר Boom קוטר גדול — בלאי אטם גורם לצניחת זרוע.\n"
            "   בדיקה: הרם Boom, כבה מנוע, המתן 10 דקות — ירידה > 100 מ\"מ = אטם פנימי.\n"
            "   פתרון: Seal Kit לגלינדר Boom R380 — עבודה של ~6 שעות."
        ),
        "metadata": {"source": "seed", "topic": "מחפרון גדול,הידראוליקה", "equipment": "R300LC-9,R320LC-9,R380LC-9", "symptom": "אסימטריה משאבות,זרוע צונחת,כלי יורד במדרון", "brand": "Hyundai"}
    },
    {
        "id": "hyundai_maintenance_r220_008",
        "text": (
            "לוח תחזוקה מחפרון יונדאי R220LC-9 - לפי שעות עבודה\n\n"
            "תחזוקה יומית — לפני משמרת:\n"
            "- בדוק מפלס שמן מנוע Cummins QSB6.7 (בין L ל-H)\n"
            "- בדוק מפלס קירור — מיכל הרחבה (בין MIN ל-MAX)\n"
            "- בדוק שמן הידראולי — Sight Glass על מיכל (צד ימין)\n"
            "- בדוק Water Separator (מיכל שקוף על מסנן הדלק) — נקה מים\n"
            "- בדוק מפלס DEF/AdBlue — מיכל נפרד (צד שמאל)\n"
            "- שמן נקבי גריז יומיים: Bucket Pins (4) + Arm Pins (4) — גריז EP2\n\n"
            "כל 250 שעות:\n"
            "- החלף שמן מנוע Cummins (15W-40 CES20086, 18 ליטר) + פילטר שמן\n"
            "- החלף מסנן דלק ראשי (Primary Fuel Filter)\n"
            "- שמן Swing Bearing — 8 נקבי גריז EP2\n"
            "- שמן Boom Foot Pin, Arm Cylinder Pins, Bucket Cylinder Pins\n\n"
            "כל 500 שעות:\n"
            "- החלף פילטר Return Line הידראולי\n"
            "- החלף מסנן דלק משני (Secondary Fuel Filter)\n"
            "- בדוק Turbocharger — שמן, רפיון ציר (Shaft Play), נזילות\n"
            "- בדוק Track Tension — רפיון 20–30 מ\"מ\n\n"
            "כל 1000 שעות:\n"
            "- בדוק ורענן שמן Final Drive (SAE 80W-90 GL-4, 4.0 ליטר לצד)\n"
            "- בדוק שמן Swing Gear Box (GL-4 80W, 2.6 ליטר)\n"
            "- בדוק Track Shoe Bolts — הידוק 380 Nm\n"
            "- בדוק EGR Valve — נקה מלכלוך\n\n"
            "כל 2000 שעות:\n"
            "- החלף שמן הידראולי (Hyundai HVI 46, 170 ליטר)\n"
            "- החלף שמן Final Drive שני הצדדים\n"
            "- החלף שמן Swing Gear Box\n"
            "- בדוק Swing Bearing — רפיון אנכי מקסימום 3 מ\"מ\n"
            "- נקה DPF / בדוק צורך ב-Thermal Cleaning"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "R220LC-9,R210LC-9", "symptom": "תחזוקה", "brand": "Hyundai"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Hyundai entries. Total KB: {rag.count()} chunks")
