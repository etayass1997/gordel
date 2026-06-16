"""Script to add brand-specific entries to the Gordel knowledge base."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

BRAND_ENTRIES = []

# ============================================================
# KOMATSU — 12 entries
# ============================================================
BRAND_ENTRIES += [
    {
        "id": "komatsu_excavator_hydraulic_001",
        "text": """תקלות הידראוליקה במחפרוני Komatsu PC300/PC360/PC390

מחפרוני סדרת PC300 של Komatsu משתמשים במשאבה כפולה ממושכנת (Tandem Piston Pump) עם בקר אלקטרוני מסוג CLSS (Closed-center Load Sensing System).

תסמינים נפוצים ופתרונות:

1. אין כוח בבום (Boom) או בזרוע (Arm) — ביצועים חלשים
   הסבר: מערכת CLSS תלויה בלחץ חישה (Sensing Pressure) שמועבר מה-Control Valve חזרה למשאבה.
   אבחון: מד לחץ בכניסת Control Valve — לחץ עבודה צריך להיות 315–350 bar ב-PC300.
   בדוק גם לחץ Pilot: 35–40 bar. אם נמוך, בדוק Pilot Pump ומסנן Pilot.
   קוד שגיאה: E03-1 (Low Pilot Pressure) — מופיע בלוח המחשב של Komatsu.
   פתרון: בדוק Pilot Filter, שסתום ההפחתה של Pilot (Pilot Relief Valve).

2. דליפה פנימית בגלינדרים — הבום "נופל"
   בדיקה: הרם בום לגובה מרבי, כבה מנוע, המתן 10 דקות.
   ירידה מעל 30mm/10 דקות = דליפה פנימית בגלינדר (Boom Cylinder).
   פתרון: פרק גלינדר, החלף ערכת חותמות (Seal Kit) — כולל Piston Seal, Rod Seal, Wiper Seal.

3. Pump Regulator לא מגיב
   תסמין: מנוע נטען מעל הנדרש, או משאבה נשארת בלחץ גבוה גם ללא עומס.
   אבחון: בדוק חוטי Solenoid Valve של Regulator — תקלת חוט פתוח (Open Circuit).
   פתרון: החלף Solenoid Valve של משאבה, בדוק בקר EPC (Electronic Pump Control).""",
        "metadata": {"source": "seed", "topic": "הידראוליקה", "equipment": "PC300,PC360,PC390", "symptom": "ביצועים חלשים,דליפה הידראולית", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_excavator_engine_001",
        "text": """תקלות מנוע Komatsu PC360 — מנוע SAA6D114E

ה-PC360LC-11 מצויד במנוע Komatsu SAA6D114E-5 עם טכנולוגיית Common Rail ועמידה בתקן פליטה Tier 4 Final.

קודי שגיאת מנוע נפוצים:

1. קוד CA2185 — לחץ Common Rail גבוה מהנדרש
   תסמין: מנוע מגיע ל-Limp Mode, הספק נפגע.
   גורמים: Pressure Limiter פגום, IMV (Inlet Metering Valve) תקוע.
   אבחון: בדוק עם Komatsu KDIAG לקריאת ערכי Common Rail בזמן אמת.
   פתרון: נקה IMV בממיס. אם הלחץ עדיין חורג — החלף Pressure Limiter.

2. קוד CA271 — חיישן טמפרטורת פליטה (Exhaust Gas Temperature Sensor)
   מאפיין: קשור למערכת DPF (Diesel Particulate Filter) ב-Tier 4.
   תסמין: אינדיקטור DPF כבוי/דולק, כוח מנוע מוגבל.
   פתרון: בדוק חיבורי חיישן EGT, החלף חיישן אם פגום. וודא שה-DPF לא סתום.

3. קוד CA111 — ECM כשל פנימי (Internal ECM Fault)
   פתרון: עדכן Firmware דרך KDIAG, אם חוזר — החלף ECM.

4. רעידות מנוע / Misfiring
   גורם נפוץ: Injector פגום (Piezo Injector או Solenoid Injector).
   אבחון: הרץ Injector Compensation Test דרך KDIAG.
   פתרון: ניקוי אולטרסוניקה, כיול מחדש (Coding), או החלפה.""",
        "metadata": {"source": "seed", "topic": "מנוע", "equipment": "PC360,PC390", "symptom": "קוד שגיאה,ביצועים נמוכים", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_mini_excavator_001",
        "text": """תקלות מיני-מחפרון Komatsu PC30/PC55/PC88

מיני-מחפרוני Komatsu מסדרה זו מצוידים במנועי 3 ו-4 צילינדר (Yanmar/Komatsu) עם מערכת הידראוליקה Fixed Displacement.

1. PC30 — הידראולי לא מגיב / ג'ויסטיק לא פועל
   אבחון: בדוק לחץ Pilot — ב-PC30 צריך להיות 27–32 bar.
   אם Pilot Pump (Charge Pump) לא בונה לחץ — ג'ויסטיק לא פועל.
   פתרון: החלף Pilot Pump (חלף קטן בגב המשאבה הראשית).

2. PC55 — רעש מאזור Swing ב-PC55MR
   תסמין: קריאה חריפה בסיבוב שמאלה/ימינה.
   גורם: Swing Bearing חסר שימון — מרווח שימון: כל 100 שעות.
   פתרון: מלא גריז ב-Swing Bearing Grease Fitting על טבעת הסיבוב.
   אם הרעש ממשיך — בדוק שחיקת Swing Pinion (שיניים).

3. PC88 — כלי לא נוסע / Travel לא מגיב
   מאפיין: ה-PC88MR-10 מצויד ב-2-Speed Travel Motor.
   בדוק: שסתום בחירת מהירות (Hi/Lo Travel) — Solenoid יכול להיות תקוע.
   קוד שגיאה: E03 (Travel Pressure Fault).
   פתרון: בדוק Solenoid Valve Hi-Lo Travel, בדוק Travel Motor לדליפות פנימיות.

4. כלל הסדרה — מנוע לא עולה בקור
   בדוק Glow Plugs (נרות להט): במנועי 3 צילינדר — 3 נרות.
   בדיקה: מד אמפר — כל נר צריך למשוך 8–15A. אם לא — נר פגום.
   פתרון: החלף נרות להט לפני עונת הסתיו.""",
        "metadata": {"source": "seed", "topic": "מנוע,הידראוליקה,נסיעה", "equipment": "PC30,PC55,PC88", "symptom": "לא מגיב,רעש,לא נוסע", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_wheel_loader_001",
        "text": """תקלות שופל גלגלים Komatsu WA380/WA470

ה-WA380-8 וה-WA470-8 הם שופלים כבדים עם מנוע Komatsu SAA6D140 ותיבת הילוכים אוטומטית (Powershift Transmission).

1. תיבת הילוכים לא מחליפת הילוך
   קוד שגיאה: T/M Fault E03 — נפוץ ב-WA470.
   גורמים:
   א. שמן Transmission נמוך — בדוק Dipstick כשהמנוע פועל ב-NEUTRAL.
   ב. Solenoid Shift Valve תקוע — תיבה נשארת בהילוך אחד.
   ג. Torque Converter לחץ נמוך.
   אבחון: חבר Komatsu VHMS (Vehicle Health Monitoring System).
   פתרון: בדוק מסנן Transmission, החלף Solenoid Valve הרלוונטי.

2. היגוי כבד / לחץ Steering נמוך
   בדוק: Steering Pump לחץ — WA470 צריך 175–210 bar.
   בדוק מסנן היגוי (Steering Filter) — סתום = ירידת לחץ.
   פתרון: נקה/החלף מסנן. אם לחץ עדיין נמוך — בדוק Steering Pump.

3. בלמים לא עוצרים / Brake Fade
   מערכת: בלמי דיסקים רטובים (Wet Disc Brakes) בתוך צירי ההנעה.
   אבחון: בדוק לחץ Brake Accumulator — צריך להיות 16–22 bar.
   בדוק שמן בלמים — אם מזוהם = החלף, כלול בדיקת Brake Disc.
   תסמין: בלמים "רכים", עצירה ארוכה מהרגיל.

4. שמן קצף בתיבת ההילוכים
   גורם: מים חדרו לשמן Transmission (Coolant Contamination).
   בדיקה: שמן ורוד ומקציף = מים.
   פתרון: פרק תיבה, נקה, בדוק Oil Cooler — כשל Heat Exchanger נפוץ.""",
        "metadata": {"source": "seed", "topic": "הילוכים,היגוי,בלמים", "equipment": "WA380,WA470", "symptom": "תיבת הילוכים,היגוי כבד,בלמים", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_compact_track_loader_001",
        "text": """תקלות Komatsu SK820 — מטען זחלים קומפקטי (Compact Track Loader)

ה-SK820-7 מצויד במנוע Kubota V3307 ומערכת הנעה Hydrostatic Drive (שני מנועי הידראוליקה לשני הזחלים).

1. כלי לא נוסע / Hydrostatic Drive תקוע
   מאפיין: Tandem Hydrostatic Pump — משאבה אקסיאלית כפולה לכל זחל בנפרד.
   תסמין: הכלי נסחף לצד אחד, או זחל אחד לא מסתובב.
   אבחון: בדוק לחץ Drive Loop בכל צד — צריך להיות זהה (350–420 bar בעומס).
   גורם נפוץ: Charge Pressure נמוך (Charge Pump שחוק) = Cavitation.
   פתרון: בדוק Charge Pressure (20–30 bar), החלף Charge Filter.

2. זרועות הרמה (Lift Arms) לא עולות / חלשות
   בדוק: לחץ Loader Circuit — צריך 240–260 bar.
   גורם: Control Valve שחוק, או Relief Valve כוונון שגוי.
   פתרון: בדוק וכוון Relief Valve. החלף Control Valve אם שחוק.

3. Aux Hydraulics לא פועל (לאביזרים: Bucket Tilt, Hammer)
   בדוק: Solenoid Valve Aux (מאחורי הכסא, בבלוק הוולוים).
   לוח: מוצג "AUX FAULT" — בדוק Joystick Aux Switch.
   פתרון: החלף Solenoid Aux Valve, בדוק חיבורי חשמל.

4. Safety Interlock — ג'ויסטיק לא מגיב
   מאפיין: ה-SK820 מצויד ב-Interlock Safety System — דלת/Safety Bar לא סגורים = מנגנוני עבודה מנוטרלים.
   תסמין: ג'ויסטיק לא מגיב למרות שהמנוע פועל.
   בדוק: מיקרוסוויץ' של דלת/Safety Bar.
   פתרון: התאם/החלף מיקרוסוויץ'.""",
        "metadata": {"source": "seed", "topic": "הידראוליקה,נסיעה,חשמל", "equipment": "SK820", "symptom": "לא נוסע,זרועות חלשות,Aux לא עובד", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_e_codes_001",
        "text": """קודי שגיאה (E-Codes / CA-Codes) נפוצים — מחפרוני Komatsu PC

Komatsu מחלקת קודי שגיאה לקטגוריות לפי תחום. קריאה דרך KDIAG או SA-2 Checker.

קודי מנוע (CA-codes — J1939):
• CA111 — ECM כשל פנימי. פתרון: עדכן Firmware, אם חוזר — החלף ECM.
• CA122 — לחץ Boost נמוך (Boost Pressure Sensor Low). בדוק Turbocharger, Intercooler.
• CA234 — מהירות מנוע גבוהה מהגבול (Engine Overspeed). בדוק Governor.
• CA271 — EGR Valve תקוע (מנועי Tier 4). נקה EGR Valve.
• CA2185 — לחץ Common Rail גבוה. בדוק IMV, Pressure Limiter.

קודי הידראוליקה ומכונה (E-codes):
• E03-1 — לחץ Pilot נמוך. בדוק Pilot Pump, Pilot Filter, Pilot Relief Valve.
• E03-3 — לחץ הידראולי ראשי נמוך. בדוק משאבה ראשית, Relief Valve.
• E10-1 — טמפרטורת שמן הידראולי גבוהה (מעל 102C). בדוק Oil Cooler, מאוורר, רמת שמן.
• E15-1 — שגיאת Pump Control Solenoid. בדוק Solenoid ו-EPC Valve.
• E19-1 — שגיאת חיישן Swing. בדוק Swing Sensor ו-Swing Parking Brake.

קודי חשמל ותקשורת:
• E30-1 — תקשורת CAN Bus נותקה. מד התנגדות CAN — צריך 60 אוהם.
• DTC P0190 — חיישן לחץ Common Rail פגום. החלף Rail Pressure Sensor.
• E30-1 — שגיאת Monitor Controller. בדוק חיבורי חשמל ל-Monitor Panel.""",
        "metadata": {"source": "seed", "topic": "קודי שגיאה", "equipment": "PC300,PC360,PC390,PC30,PC55,PC88", "symptom": "קוד שגיאה E-code CA-code", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_travel_undercarriage_001",
        "text": """מערכת נסיעה ותשתית תחתית — Komatsu PC300/PC360

Undercarriage של PC300/PC360 כולל: Travel Motor, Final Drive, Track Roller, Carrier Roller, Idler, Sprocket, וזחלים (Track Shoes).

1. PC300 — לא נוסע לכיוון ספציפי (אסימטריה)
   אבחון: בדוק לחץ Travel Circuit בכל צד עם T-fitting.
   לחץ נורמלי PC300: 350–420 bar בנסיעה עם עומס.
   פתרון: החלף Travel Motor (Orbital Hydraulic Motor) של הצד החלש.

2. זחל נופל תכופות — PC360
   כוונון נכון: מדוד Sag בזחל בין Carrier Roller ל-Idler.
   PC360: 10–30mm Sag תלוי בתנאי קרקע.
   כוונון: הוסף גריז ל-Track Tension Cylinder דרך Grease Fitting על Idler Adjuster.
   שחרור: Breather Valve אם מתח יתר.

3. Carrier Roller שבור — PC300
   תסמין: קצה הזחל "מתרומם", רטט חריג.
   פתרון: החלף Roller. לפני החלפה — שחרר מתח זחל לגמרי.

4. Sprocket שחוק — PC360LC
   מדידה: עובי שן — אם פחות מ-12mm (מ-18mm מקורי) = החלף.
   המלצה: החלף Sprocket ו-Track Chain ביחד.

5. Final Drive Oil — PC300/PC360
   מרווח בדיקה: כל 500 שעות (לפי מדריך Komatsu).
   שמן מפרט: SAE 80W-90 GL-5 (2.1 ליטר לכל Final Drive ב-PC300).
   סימן כשל: שמן חלבי = מים נכנסו דרך Floating Seal פגום.""",
        "metadata": {"source": "seed", "topic": "נסיעה,תשתית תחתית", "equipment": "PC300,PC360", "symptom": "לא נוסע,זחל נופל,Final Drive", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_can_electrical_001",
        "text": """תקלות CAN Bus וחשמל — Komatsu PC390/PC360 Generation 11

ארכיטקטורת CAN ב-Gen-11:
• Engine CAN (J1939) — בין ECM לבקר מכונה
• Machine CAN — בין Monitor, Pump Controller, Valve Controller
• Komtrax CAN — יחידת טלמטריה לאינטרנט

1. קוד E30 — תקשורת CAN נותקה בין Monitor לבקר
   תסמין: מסך Monitor מכבה/מאפס, נתונים נעלמים.
   אבחון: בדוק קונקטורים CN-S01/CN-S02 ב-Monitor Panel.
   מדוד התנגדות: CAN-H לCAN-L = 120 אוהם בכל קצה (60 אוהם במקביל).
   פתרון: בדוק כבל CAN לפציעה. אם Terminator פגום — החלף.

2. קודים מרובים בו זמנית — False Codes
   גורם: קצר לקרקע (Short to Ground) בכבל CAN משותף.
   אבחון: נתק בקרים אחד אחד — כשהקודים נעלמים זיהית הכשל.
   פתרון: תיקון בידוד כבל, Wire Harness Repair.

3. Monitor Panel מת — PC390
   בדוק נתיך F-1 (לוח נתיכים תחתון שמאל) — לעיתים שרוף.
   בדוק מתח 24V ב-Monitor Connector Pin-1.
   פתרון: החלף נתיך, אם חוזר — חפש Short Circuit בכבל.

4. קוד E15 — EPC Solenoid Fault (Electronic Pump Control)
   תסמין: משאבה תקועה על לחץ גבוה — מנוע עומס יתר.
   אבחון: מד התנגדות Solenoid — צריך 10–15 אוהם. אם OL = כשל.
   פתרון: החלף EPC Solenoid Valve על המשאבה.""",
        "metadata": {"source": "seed", "topic": "חשמל,CAN Bus", "equipment": "PC360,PC390", "symptom": "תקשורת CAN,קודי שגיאה,Monitor כבוי", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_swing_pump_001",
        "text": """מנגנון סיבוב ומשאבה — Komatsu PC300/PC390

מנגנון Swing כולל: Swing Motor, Swing Gearbox, Swing Bearing, Swing Lock (Parking Brake).

1. סיבוב חלש — PC300-8
   אבחון: בדוק לחץ Swing Relief — צריך 230–250 bar.
   כוונון Swing Relief Valve: מפתח 27mm + מד לחץ, כוונן ב-5 bar בכל פעם.
   גורם נוסף: Swing Motor פגום — דליפה פנימית מפחיתה מומנט.
   בדיקת Motor: Drain Flow מעל 10 L/min = החלף Swing Motor.

2. Swing Gearbox — שמן ומפלס
   שמן: SAE 90 Gear Oil (כ-3.5 ליטר ב-PC300).
   מרווח: בדיקה כל 500 שעות, החלפה כל 2000 שעות.
   תסמין לכשל: ריח חרוך מאזור Gearbox, רעש טחינה.

3. Swing Brake לא משתחרר
   מאפיין: Negative Brake — פעיל כברירת מחדל, משתחרר בלחץ Pilot.
   תסמין: כלי לא יכול להסתובב, רעש חיכוך.
   אבחון: בדוק לחץ Pilot ל-Swing Brake Release — צריך 30–35 bar.
   פתרון: בדוק Solenoid Valve של Swing Brake.

4. Swing Bearing — בדיקת שחיקה ב-PC360
   מתודה: מדידת Clearance עם Dial Gauge.
   גבול שחיקה: מעל 3.0mm Radial Play = החלף Bearing.
   שימון: Grease Nipples על הטבעת — כל 100 שעות (Komatsu Grease G2).""",
        "metadata": {"source": "seed", "topic": "מנגנון סיבוב,משאבה", "equipment": "PC300,PC390,PC360", "symptom": "סיבוב חלש,בלם סיבוב,Swing Bearing", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_maintenance_schedule_001",
        "text": """לוח תחזוקה מפורט — Komatsu PC300-8 / PC360-11

תחזוקה יומית (Daily — לפני כל משמרת):
• בדוק מפלס שמן מנוע — Dipstick בין MIN ל-MAX
• בדוק מפלס קירור — Coolant Reservoir
• בדוק מפלס שמן הידראולי — Sight Glass בצד מיכל
• נקה Water Separator מדי בוקר
• בדוק Pre-cleaner (מוציא אבק ראשוני)
• בדוק מתח זחלים — 10–30mm Sag לפי PC300/PC360
• שמן יומי: Bucket Pin, Stick-to-Bucket Link Pin

תחזוקה כל 50 שעות:
• שמן: Boom Foot Pin, Boom/Arm/Bucket Cylinder Pins
• בדוק Swing Bearing Grease Level

תחזוקה כל 250 שעות:
• החלף שמן מנוע: Komatsu EO15W-40 (כ-28 ליטר ב-PC300)
• החלף Engine Oil Filter + Fuel Filter Primary ו-Secondary
• בדוק Drive Belt למתח ושחיקה

תחזוקה כל 500 שעות:
• החלף Hydraulic Oil Filter (Return Filter + Pilot Filter)
• בדוק/החלף Air Cleaner Element
• בדוק Final Drive Oil Level

תחזוקה כל 1000 שעות:
• החלף שמן הידראולי מלא (Komatsu HPDO46)
• בדוק Fuel Injectors — Injector Compensation Test ב-KDIAG
• החלף Swing Gearbox Oil

תחזוקה כל 2000 שעות:
• החלף Final Drive Oil (SAE 80W-90)
• בדוק Swing Bearing — Radial Play Test
• בדוק Coolant — PH ועמידות קפיאה""",
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "PC300,PC360", "symptom": "תחזוקה,מרווחים", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_wa470_transmission_001",
        "text": """מערכת הנעה וגיר — Komatsu WA470-8 (שופל גלגלים)

ה-WA470-8 מצויד ב-Powershift Transmission עם Torque Converter, 4 הילוכים קדימה ו-3 אחורה, ומערכת KMX (Komatsu Modulated Clutch).

1. Lock-Up לא פועל
   תסמין: סיבובי מנוע גבוהים גם בנסיעה יציבה — Lock-Up לא נכנס.
   קוד: T/M E-04 — בדוק עם Komatsu VHMS.
   גורם: Solenoid Lock-Up Valve פגום, לחץ נמוך.
   פתרון: בדוק Solenoid (חשמל + לחץ), בדוק T/M Filter.

2. החלקת גיר (Clutch Slipping) — WA470
   תסמין: מנוע עולה אך כלי לא מאיץ.
   אבחון: בדוק T/M Clutch Pressure בכל הילוך — צריך 1300–1500 kPa (13–15 bar).
   גורם: Clutch Disc Pack שחוק.
   פתרון: פרק T/M, מדוד עובי Disc Pack, החלף אם מתחת ל-Minimum Thickness.

3. טמפרטורת T/M גבוהה
   בדוק: שמן T/M — Dexron-3 ATF (כ-25 ליטר ב-WA470).
   בדוק T/M Oil Cooler (Heat Exchanger) לסתימות.

4. Differential Lock לא נכנס — WA380/WA470
   תסמין: לחיצה על Diff Lock — לא מרגיש נעילה.
   אבחון: בדוק Solenoid Valve Diff Lock, בדוק לחץ אוויר/הידראולי.
   פתרון: בדוק Solenoid, Shift Fork פנימי ב-Axle.""",
        "metadata": {"source": "seed", "topic": "גיר,הנעה,צירים", "equipment": "WA470,WA380", "symptom": "גיר לא עובד,Clutch,Diff Lock", "brand": "Komatsu"}
    },
    {
        "id": "komatsu_dpf_tier4_001",
        "text": """מערכת טיפול בפליטה DPF/SCR — Komatsu PC360-11 / PC390-11 (Tier 4 Final)

מחפרוני Komatsu Gen-11 עומדים בתקני Tier 4 Final/Stage V באמצעות:
• EGR (Exhaust Gas Recirculation)
• DPF (Diesel Particulate Filter)
• SCR עם DEF/AdBlue (בחלק מהדגמים)

1. DPF סתום — אינדיקטור DPF דולק
   קוד: CA3719 (DPF High Soot Level).
   פתרון מיידי: Passive Regeneration — הרץ מנוע ב-1800+ RPM ללא עומס 30–60 דקות.
   אם לא עוזר: Active Forced Regeneration דרך KDIAG (מחמם DPF ל-600C+).
   אם DPF עדיין סתום: שטיפה מקצועית או החלפה.

2. קוד CA2795 — EGR Valve תקוע
   תסמין ב-Closed: עשן שחור, טמפרטורת פליטה גבוהה.
   תסמין ב-Open: מנוע מתקשה, עשן לבן/אפור בסרלנטי.
   פתרון: ניקוי EGR Valve מפיח, אם לא — החלפה.

3. DEF/AdBlue — קוד CA4364 (DEF Quality Fault)
   גורם: AdBlue מזוהם או ריכוז לא תקין (צריך 32.5% Urea).
   פתרון: רוקן מיכל, שטוף, מלא AdBlue חדש מאריזה מקורית.

הערה: אל תכבה מנוע מיד לאחר עבודה כבדה — תן Cooldown של 3–5 דקות בסרלנטי, במיוחד לאחר Regeneration.""",
        "metadata": {"source": "seed", "topic": "פליטה,DPF,Tier4", "equipment": "PC360,PC390", "symptom": "DPF סתום,EGR תקוע,AdBlue", "brand": "Komatsu"}
    },
]

# Add all entries
added = 0
for entry in BRAND_ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} entries. Total KB: {rag.count()} chunks")
