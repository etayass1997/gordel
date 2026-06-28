"""Add Hitachi knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "hitachi_excavator_hydraulic_zx200_zx330_001",
        "text": (
            "היטאצ'י ZX200 / ZX225 / ZX330 - תקלות הידראוליקה\n\n"
            "מחפרוני היטאצ'י סדרת ZX (Zaxis) מצוידים במשאבת פיסטון כפולה HPV145 (ZX225) או HPV210 (ZX330).\n"
            "מערכת ה-Negative Flow Control (NFC) — ייחודית להיטאצ'י — שולטת בספיקת המשאבה.\n\n"
            "1. אובדן כוח הידראולי — כלי איטי\n"
            "   לחץ מערכת ZX225: 34.3 MPa (343 בר). ZX330: 35 MPa (350 בר).\n"
            "   בדיקה: חבר מד לחץ לנקודת בדיקה G1 (Main Pump 1) ו-G2 (Main Pump 2).\n"
            "   גורם נפוץ: NFC Relief Valve לא מכוון — בדוק לחץ NFC: 3.0 MPa (30 בר) בעמדת ניוטרל.\n"
            "   פתרון: כוון NFC Relief Valve ב-Main Control Valve לפי נתוני היטאצ'י.\n\n"
            "2. Pump Horsepower Control לא פועל\n"
            "   ZX225/ZX330 עם מערכת בקרת כוח (Power Optimization) — מגביל משאבה לפי עומס מנוע.\n"
            "   גורם: חיישן לחץ Engine Pump Absorption פגום.\n"
            "   קוד: 04-5 (Pump Control Pressure Sensor) — בדוק דרך Dr. ZX.\n\n"
            "3. שמן הידראולי חם (Oil Overheating)\n"
            "   ZX225: גבול אזהרה 95°C. גבול כיבוי 105°C.\n"
            "   גורם: Oil Cooler סתום — נקה עם מים בלחץ נמוך, מהפנים החוצה.\n"
            "   בדיקה Dr. ZX: Monitor → Oil Temperature.\n\n"
            "4. Arm/Boom איטיים לאחד הצדדים\n"
            "   גורם: Travel Straight Spool ב-MCV מסונכרן — בדוק תנוחת Spool.\n"
            "   ZX330: פרק MCV, בדוק ונקה כל Spool לתנועה חופשית."
        ),
        "metadata": {"source": "seed", "topic": "הידראוליקה,NFC", "equipment": "ZX200,ZX225,ZX330", "symptom": "כלי איטי,שמן חם,לחץ נמוך", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_dr_zx_diagnostic_002",
        "text": (
            "מערכת אבחון Dr. ZX (Hitachi Diagnostic Tool) — מחפרוני היטאצ'י\n\n"
            "Dr. ZX הוא כלי האבחון הרשמי של היטאצ'י לסדרת Zaxis.\n"
            "חיבור: ממשק USB→Ethernet לשקע Deutsch 9-pin ליד מושב הנהג.\n\n"
            "מבנה קטגוריות ב-Dr. ZX:\n"
            "- Monitor: צפייה בחיישנים בזמן אמת (שמן, לחץ, טמפרטורה, RPM)\n"
            "- Fault: קריאה ואיפוס קודי שגיאה DTC\n"
            "- Active Check: הפעלת סולנואידים ורכיבים לבדיקה\n"
            "- Adjustment: כיול חיישנים ופרמטרים\n\n"
            "קודי שגיאה נפוצים (DTC) בהיטאצ'י ZX:\n"
            "- 02-1: חיישן לחץ Pilot (Pilot Pressure Sensor Fault)\n"
            "- 02-3: חיישן זווית Boom (Boom Angle Sensor)\n"
            "- 03-2: טמפרטורת שמן הידראולי גבוהה\n"
            "- 04-1: חיישן לחץ Pump 1 פגום\n"
            "- 04-5: חיישן בקרת הורסאות משאבה\n"
            "- 08-1: מנוע — לחץ שמן נמוך\n"
            "- 08-3: מנוע — טמפרטורת קירור גבוהה\n"
            "- 12-1: תקשורת CAN Bus — Engine ECU לא מגיב\n"
            "- 15-1: Swing — Over Speed Detection\n\n"
            "קודים מרובים בו-זמנית:\n"
            "גורם שכיח: מתח סוללה נמוך (< 22V).\n"
            "בדיקה: Monitor → Electrical → Battery Voltage.\n"
            "אם מתח תקין — בדוק CAN Bus Termination Resistors (120 אוהם כל קצה, 60 אוהם ביחד)."
        ),
        "metadata": {"source": "seed", "topic": "אבחון Dr. ZX", "equipment": "ZX200,ZX225,ZX330,ZX350", "symptom": "קודי שגיאה,אבחון", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_excavator_engine_isuzu_003",
        "text": (
            "מנועי Isuzu AI-4JJ1 / 6HK1 במחפרוני היטאצ'י ZX\n\n"
            "היטאצ'י משתמשת במנועי Isuzu:\n"
            "- ZX200/ZX225: Isuzu AI-4JJ1 (4 צילינדרים, 5.2 ליטר, 128 כ\"ס)\n"
            "- ZX330/ZX350: Isuzu AI-6HK1 (6 צילינדרים, 7.8 ליטר, 222 כ\"ס)\n"
            "- ZX490: Isuzu AJ-6WG1 (6 צילינדרים, 9.8 ליטר, 308 כ\"ס)\n\n"
            "1. מנוע לא מגיע ל-RPM מלא\n"
            "   גורם א: EGR Valve סתום/פגום — מחזיר יותר מדי גזים.\n"
            "   קוד Dr. ZX: DTC P0401 = EGR Flow Insufficient.\n"
            "   פתרון: נקה EGR Valve ו-EGR Cooler בספריי מנקה.\n"
            "   גורם ב: Throttle Control Actuator בעיה.\n"
            "   קוד: P2100 = Throttle Actuator Circuit Fault.\n\n"
            "2. עשן לבן/כחול בהזנקה בקור\n"
            "   גורם: Glow Plugs (נרות להט) שחוקים ב-Isuzu 4JJ1.\n"
            "   בדיקה: מדוד אמפר לכל נר — תקין: 15–18A.\n"
            "   גורם נוסף: מחלפי חום (EGR Cooler) דולפים — שמן בצנצנת הקירור.\n\n"
            "3. DPF מלא — Regen נדרש (ZX225/ZX330 מסוף 2013)\n"
            "   נורת DPF כתומה = Regen אוטומטי מתבצע — אפשר להמשיך לעבוד.\n"
            "   נורת DPF אדומה מהבהבת = עצור ובצע Stationary Regen!\n"
            "   Dr. ZX: Active Check → DPF Forced Regeneration.\n"
            "   אזהרה: אל תבצע Regen ליד עשב/חומרים דליקים.\n\n"
            "4. AdBlue (SCR) Fault\n"
            "   קוד: DTC P20EE = SCR NOx Catalyst Efficiency.\n"
            "   גורם נפוץ: DEF Injector גובש (Crystallized).\n"
            "   פתרון: Purge Cycle דרך Dr. ZX, אם לא עוזר — פרק ונקה Injector במים חמים."
        ),
        "metadata": {"source": "seed", "topic": "מנוע Isuzu,DPF,AdBlue", "equipment": "ZX225,ZX330,ZX350,ZX490", "symptom": "חוסר כוח,עשן,DPF", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_excavator_swing_travel_004",
        "text": (
            "היטאצ'י ZX330 / ZX350 - מערכת סיבוב ונסיעה\n\n"
            "סיבוב ZX330:\n"
            "- Swing Motor: Kawasaki MFC270 Piston Motor\n"
            "- לחץ סיבוב מקסימום: 28.4 MPa (284 בר)\n"
            "- שמן גיר סיבוב (Swing Reduction Gear): GL-4 80W — 2.8 ליטר\n"
            "- Swing Bearing: שימון כל 250 שעות — גריז EP2 NLGI-2\n\n"
            "1. סיבוב לא עוצר בחדות (Swing Drift)\n"
            "   גורם: Swing Brake Valve לא מחזיק.\n"
            "   בדיקה: הסר ג'ויסטיק ← אם הכלי ממשיך לסוב = Swing Brake Valve פגום.\n"
            "   פתרון: החלף Swing Brake Valve Assembly.\n\n"
            "2. קול חריקה בסיבוב\n"
            "   גורם: Swing Bearing יבש — לא שומן לזמן רב.\n"
            "   פתרון: שמן מיידי (9 נקבי גריז ב-ZX330), בדוק אם יש שחיקה גלויה על השיניים.\n\n"
            "3. Swing Gear Box שומן דולף\n"
            "   ZX330: Gear Box Seal תחתון — בדוק O-ring Drain Plug.\n\n"
            "נסיעה ZX330:\n"
            "- Travel Motor: Piston Type, לחץ מקסימום 40 MPa (400 בר)\n"
            "- Final Drive: 2-Speed, שמן SAE 80W-90 GL-4 — 3.8 ליטר לצד\n\n"
            "4. כלי 'מתיישר' לאחד הצדדים בנסיעה\n"
            "   גורם: Straight Travel Valve (שסתום נסיעה ישרה) פגום.\n"
            "   ZX330: שסתום נפרד ב-MCV שמסנכרן את שני Travel Motors.\n"
            "   פתרון: נקה Straight Travel Spool, בדוק O-rings.\n\n"
            "5. 2-Speed לא מחלף\n"
            "   גורם: Travel 2-Speed Solenoid פגום, או Pilot Pressure נמוך (< 30 בר).\n"
            "   בדיקה Dr. ZX: Active Check → 2-Speed Solenoid."
        ),
        "metadata": {"source": "seed", "topic": "סיבוב,נסיעה", "equipment": "ZX330,ZX350,ZX225", "symptom": "סיבוב לא עוצר,כלי מתיישר בנסיעה", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_zx_electrical_can_005",
        "text": (
            "חשמל ו-CAN Bus — מחפרוני היטאצ'י ZX\n\n"
            "מחפרוני ZX (מ-2013) עם ארכיטקטורת CAN Bus מרובה:\n"
            "- CAN 1 (500 kbps): Engine ECU + Pump Controller\n"
            "- CAN 2 (250 kbps): Monitor + Swing/Travel Controllers\n"
            "- CAN 3 (250 kbps): AC System + Camera System\n\n"
            "1. מסך מוניטור כבוי (Monitor Display Off)\n"
            "   גורם א: נתיך F12 (15A) שרוף — לוח נתיכים מתחת למושב מימין.\n"
            "   גורם ב: Connector CN-1 (14-pin) מאחורי המסך רופף.\n"
            "   בדיקה: וודא 24V על Pin 1 (Power) של Connector.\n\n"
            "2. Joystick לא מגיב (EH Joystick Failure)\n"
            "   ZX225/ZX330 מ-2015 עם EH Joystick (חשמלי-הידראולי).\n"
            "   קוד Dr. ZX: 02-5 = Left Joystick Signal Fault.\n"
            "   בדיקה: Monitor → Active Check → Joystick — בדוק ערכי Hall Sensor (0.5–4.5V).\n"
            "   פתרון: החלף Joystick Assembly.\n\n"
            "3. Alternator לא טוען\n"
            "   ZX225/ZX330: 24V מערכת, Alternator 80A.\n"
            "   מתח תקין במנוע דולק: 27.5–28.5V.\n"
            "   גורם: V-Belt החליק — בדוק מתח רצועה ושחיקה.\n\n"
            "4. קודי CAN Bus מרובים בבת אחת\n"
            "   בדוק: Battery Voltage → מינימום 24V בהפעלה.\n"
            "   בדוק: Termination Resistors — 60 אוהם בין CAN-H ל-CAN-L.\n"
            "   שכיח: Harness Connector שנחתך/קורוד ליד Swing Bearing Area."
        ),
        "metadata": {"source": "seed", "topic": "חשמל,CAN Bus,אבחון", "equipment": "ZX200,ZX225,ZX330,ZX350", "symptom": "מסך כבוי,Joystick לא מגיב,קודי שגיאה מרובים", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_maintenance_zx225_006",
        "text": (
            "לוח תחזוקה מחפרון היטאצ'י ZX225 - לפי שעות\n\n"
            "תחזוקה יומית — לפני משמרת:\n"
            "- בדוק מפלס שמן מנוע Isuzu 4JJ1 (מוט בין F ל-L)\n"
            "- בדוק מפלס קירור (בין LOW ל-FULL)\n"
            "- בדוק שמן הידראולי — Sight Glass על מיכל ימין אחורי\n"
            "- בדוק Water Separator — נקה אם יש מים\n"
            "- שמן נקבי גריז יומיים: Bucket Pins + Arm Pins (8 נקבים)\n\n"
            "כל 250 שעות:\n"
            "- החלף שמן מנוע (Isuzu 15W-40 CF-4, 18 ליטר) + פילטר שמן\n"
            "- החלף מסנן דלק ראשי\n"
            "- שמן Swing Bearing (9 נקבים) — גריז ZX EP2\n"
            "- שמן Boom, Arm, Bucket Foot Pins (קפסת גריז)\n\n"
            "כל 500 שעות:\n"
            "- החלף פילטר Return Line הידראולי\n"
            "- החלף Pre-Filter הידראולי (Suction Strainer)\n"
            "- בדוק Turbocharger (שמן, רפיון Shaft)\n\n"
            "כל 1000 שעות:\n"
            "- בדוק ורענן שמן Final Drive (SAE 80W-90, 3.8 ליטר לצד)\n"
            "- בדוק Swing Gear Box Oil (GL-4 80W, 2.8 ליטר)\n"
            "- בדוק Track Shoe Bolts — הידוק 340 Nm\n\n"
            "כל 2000 שעות:\n"
            "- החלף שמן הידראולי (Hitachi Super Hydraulic Oil 46, 170 ליטר)\n"
            "- החלף שמן Final Drive שני הצדדים\n"
            "- בדוק Swing Bearing — רפיון אנכי מקסימום 3 מ\"מ\n"
            "- בדוק EGR Valve ו-EGR Cooler — נקה לכלוך"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "ZX225,ZX200", "symptom": "תחזוקה", "brand": "Hitachi"}
    },
    {
        "id": "hitachi_zx490_large_excavator_007",
        "text": (
            "היטאצ'י ZX490 / ZX530 מחפרונים גדולים - תקלות ייחודיות\n\n"
            "ZX490 ו-ZX530 הם מחפרונים כבדים (49–53 טון) עם מנוע Isuzu AJ-6WG1 (308–320 כ\"ס).\n\n"
            "1. Pump 1 / Pump 2 ספיקה שונה\n"
            "   ZX490 עם 2 משאבות נפרדות — כל משאבה מפעילה מעגל נפרד.\n"
            "   אם Pump 1 חלשה: Boom + Travel Right איטיים.\n"
            "   אם Pump 2 חלשה: Arm + Swing + Travel Left איטיים.\n"
            "   בדיקה: Dr. ZX → Monitor → Main Pump Pressure 1 vs. 2.\n\n"
            "2. עלייה במשקל (Heavy Lift Mode) לא מופעל\n"
            "   ZX490 עם Power Boost (HP Mode) — לחצן על Joystick ימין.\n"
            "   Power Boost מעלה לחץ ל-38 MPa ל-8 שניות.\n"
            "   גורם כשל: Power Boost Solenoid פגום.\n"
            "   בדיקה: Dr. ZX → Active Check → Power Boost Solenoid.\n\n"
            "3. Travel Motor Counterbalance Valve — כלי יורד במדרון\n"
            "   ZX490: Counterbalance Valve מגביל ירידה חופשית במדרון.\n"
            "   תסמין: כלי 'רץ קדימה' בהורדת מדרון, ג'ויסטיק נעול.\n"
            "   פתרון: החלף Counterbalance Valve Assembly — זוג (שני הצדדים).\n\n"
            "4. Main Control Valve (MCV) זליגה פנימית\n"
            "   ZX530: Boom/Arm יורדים לאט גם כשג'ויסטיק ניוטרל.\n"
            "   בדיקה: הרם Boom לגובה מקסימום, כבה מנוע, מדוד ירידה תוך 10 דק'.\n"
            "   ירידה > 100 מ\"מ = Load Check Valve ב-MCV פגום.\n"
            "   פתרון: פרק MCV, נקה/החלף Load Check Valve."
        ),
        "metadata": {"source": "seed", "topic": "מחפרון כבד,הידראוליקה", "equipment": "ZX490,ZX530", "symptom": "אסימטריה בין משאבות,כלי יורד במדרון", "brand": "Hitachi"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Hitachi entries. Total KB: {rag.count()} chunks")
