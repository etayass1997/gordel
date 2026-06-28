"""Add Manitou knowledge base entries."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import RAGEngine

rag = RAGEngine()
print(f"KB before: {rag.count()} chunks")

ENTRIES = [
    {
        "id": "manitou_telehandler_mlt630_mlt741_001",
        "text": (
            "מאניטו MLT630 / MLT741 / MLT845 טלסקופ רב-תכליתי - תקלות הרמה והיגוי\n\n"
            "טלסקופי מאניטו סדרת MLT (Multi-Loader Telescopic) הם מכונות רב-תכליתיות\n"
            "לחקלאות ובנייה. MLT741-120 PS: הרמה מקסימום 4.1 מ', 7 טון.\n\n"
            "1. זרוע לא עולה לגובה מלא תחת עומס\n"
            "   לחץ Relief הרמה MLT741: 230 בר.\n"
            "   גורם א: Relief Valve Lift Circuit לא מכוון נכון.\n"
            "   בדיקה: חבר מד לחץ לנקודת P1 (Lift Cylinder Supply) — השווה ל-Relief Setting.\n"
            "   גורם ב: Lift Cylinder Internal Seal Leak — בדוק צניחת זרוע תוך 5 דקות.\n\n"
            "2. זרוע צונחת בניוטרל (Boom Drift)\n"
            "   גורם: Load Holding Valve (LSV) פגום בגוש שסתומים.\n"
            "   MLT630/MLT741: LSV ממוקם ב-Control Valve Block.\n"
            "   פתרון: פרק LSV, נקה Ball + Seat, החלף O-rings ואטמים.\n\n"
            "3. היגוי כבד / לא מגיב\n"
            "   MLT741 עם Hydrostatic Steering (EHPS).\n"
            "   גורם: Steering Priority Valve פגום — שמן לא מגיע לסירת היגוי.\n"
            "   בדיקה: לחץ היגוי תקין: 180–200 בר.\n"
            "   פתרון: בדוק Orbitrol (Steering Unit), בדוק Priority Valve Spool.\n\n"
            "4. כף לא מתכוננת (Attachment Not Tilting)\n"
            "   גורם: Bucket Tilt Cylinder Relief Valve לחץ נמוך.\n"
            "   לחץ תקין Tilt: 220 בר.\n"
            "   פתרון: כוון Relief Valve ב-Tilt Circuit.\n\n"
            "5. Outriggers לא יורדים (MLT הצוייד בחיצוניות)\n"
            "   גורם: Outrigger Solenoid Valve פגום.\n"
            "   בדיקה: מדוד 12V/24V על Solenoid בהפעלה.\n"
            "   פתרון: החלף Solenoid Coil."
        ),
        "metadata": {"source": "seed", "topic": "טלסקופ,הרמה,היגוי", "equipment": "MLT630,MLT741,MLT845", "symptom": "זרוע לא עולה,זרוע צונחת,היגוי כבד", "brand": "Manitou"}
    },
    {
        "id": "manitou_telehandler_mt1840_mt2150_002",
        "text": (
            "מאניטו MT1840 / MT2150 טלסקופ בנייה - תקלות זרוע טלסקופית\n\n"
            "סדרת MT (Telescopic Handler for Construction) — MT1840: גובה הרמה 18 מ', 4 טון.\n"
            "MT2150: גובה הרמה 21 מ', 5 טון. מצוידים במנוע Deutz TCD 4.1.\n\n"
            "1. זרוע טלסקופית לא מתארכת (Boom Extension Failure)\n"
            "   MT1840/MT2150: מנגנון ארכה ב-Chain/Telescopic Cylinders.\n"
            "   גורם א: גלינדר Extend Cylinder פגום — אטמים שחוקים.\n"
            "   בדיקה: לחץ צריך להיות 200 בר בעת ארכה בעומס.\n"
            "   גורם ב: Slide Pad (ריפוד גלישה) שחוק — גורם לתקיעות הזרוע.\n"
            "   פתרון: פרק Boom, בדוק ו-החלף Slide Pads בכל שלב.\n\n"
            "2. Boom Section 2 לא נארכת אבל Section 1 כן\n"
            "   גורם: שרשרת ארכה (Extension Chain) Section 2 נשברת/מתרופפת.\n"
            "   בדיקה: פתח כיסוי צד Boom, בדוק שרשרת.\n"
            "   פתרון: החלף שרשרת (Extension Chain Kit) — תמיד זוג ביחד.\n\n"
            "3. זרוע רועדת בגובה גבוה\n"
            "   גורם נפוץ: Slide Pad שחוק בשלב הראשון — עודף 'פלאי' (Play) בחיבור.\n"
            "   פתרון: החלף Slide Pads שלב 1. המחפרון לא יציב גם עם בעיה קלה!\n\n"
            "4. Carriage (מנשא כף) לא שומר עמדה (Carriage Drift)\n"
            "   גורם: Side Shift Cylinder seal פגום.\n"
            "   פתרון: Seal Kit לגלינדר Side Shift."
        ),
        "metadata": {"source": "seed", "topic": "טלסקופ,זרוע טלסקופית", "equipment": "MT1840,MT2150,MT1440", "symptom": "זרוע לא מתארכת,רעידה בגובה", "brand": "Manitou"}
    },
    {
        "id": "manitou_engine_deutz_perkins_003",
        "text": (
            "מנועי Deutz ו-Perkins בטלסקופי מאניטו - תקלות נפוצות\n\n"
            "מאניטו משתמשת בשני ספקי מנועים עיקריים:\n"
            "- Deutz TCD 3.6 / TCD 4.1: MLT630/741/845 ו-MT1440/MT1840\n"
            "- Perkins 854E-E34TA / 1204E: מדגמים ישנים יותר (לפני 2015)\n\n"
            "מנוע Deutz TCD 4.1 — מאפיינים:\n"
            "- 4 צילינדרים, 4.1 ליטר, 75–130 כ\"ס\n"
            "- Common Rail Injection\n"
            "- Stage V (אירופה) / Tier 4 Final (ארה\"ב)\n"
            "- מיוחד: מנוע מצונן אוויר (Air Cooled) בחלק מהגרסאות — ללא נוזל קירור!\n\n"
            "1. Deutz TCD מתחמם יתר על המידה\n"
            "   גרסאות מים: בדוק רדיאטור, מפלס קירור, Thermostat.\n"
            "   גרסאות אוויר (Deutz Air Cooled): בדוק Cooling Fins — חייבים להיות נקיות לחלוטין.\n"
            "   פתרון: נקה Fins בלחץ אוויר כל 100 שעות בתנאי אבק.\n\n"
            "2. Deutz SERDIA / DEERFIELD — אבחון\n"
            "   כלי אבחון רשמי: SERDIA 2010 (USB→CAN).\n"
            "   קודי שגיאה נפוצים:\n"
            "   - P0087: Rail Pressure Too Low → בדוק מסנן דלק, Lift Pump\n"
            "   - P0191: Rail Pressure Sensor Fault\n"
            "   - P0401: EGR Flow Insufficient\n"
            "   - P2453: DPF Differential Pressure High → Regen נדרש\n\n"
            "3. Perkins 854E לא עולה\n"
            "   גורם שכיח: Air Lock בדלק (כניסת אוויר לצינורות).\n"
            "   פתרון: הפעל Primer Pump (משאבת פריימינג) ידנית עד שדלק זורם ללא בועות.\n\n"
            "4. מנוע נכבה תחת עומס\n"
            "   גורם: Hydraulic Load גדול מדי מחנק מנוע.\n"
            "   בדוק: Anti-Stall System — בקר Manitou מגביל הידראוליקה אם RPM יורד.\n"
            "   פתרון: בדוק פרמטר Anti-Stall ב-Manitou Diagnostic."
        ),
        "metadata": {"source": "seed", "topic": "מנוע Deutz,Perkins", "equipment": "MLT741,MT1840,MT2150", "symptom": "התחממות,חוסר כוח,מנוע נכבה", "brand": "Manitou"}
    },
    {
        "id": "manitou_diagnostic_system_004",
        "text": (
            "מערכת אבחון Manitou — Manitou Diagnostic Tool (MDT)\n\n"
            "מאניטו מציעה כלי אבחון ייעודי: MDT (Manitou Diagnostic Tool), גרסאות עדכניות עם אפליקציית Manitou Diag.\n\n"
            "חיבור:\n"
            "1. חבר ממשק USB→CAN (Manitou Adapter) לשקע OBD/Deutsch ליד מושב המפעיל.\n"
            "2. פתח Manitou Diag, בחר Machine Model ו-S/N.\n"
            "3. כנס ל-Diagnostic → Faults לקריאת קודי DTC.\n\n"
            "בקרים עיקריים (ECU) במאניטו MLT/MT:\n"
            "- Engine ECU: קודי מנוע Deutz/Perkins\n"
            "- Transmission ECU: גיר ZF, קודי שידור\n"
            "- Hydraulic Controller: שסתומים, לחצים, טמפרטורות\n"
            "- Display/Monitor ECU: בקר תצוגה ולוח בקרה\n\n"
            "קודי שגיאה נפוצים מאניטו:\n"
            "- Fault 0001: Joystick Signal Out of Range\n"
            "- Fault 0010: Hydraulic Oil Temperature High (> 100°C)\n"
            "- Fault 0021: Load Moment Indicator — Overload Warning\n"
            "- Fault 0031: Transmission Oil Temperature High\n"
            "- Fault 0042: Rear Axle Angle Sensor Fault\n"
            "- Fault 0055: CAN Bus Communication Failure\n"
            "- Fault 0061: Engine ECU Not Responding\n\n"
            "Active Tests:\n"
            "- בדוק כל סולנואיד בנפרד\n"
            "- כייל חיישני זווית (Angle Sensors)\n"
            "- כייל Load Moment Indicator (LMI)\n"
            "- קרא Live Data: לחץ, ספיקה, טמפרטורה, RPM"
        ),
        "metadata": {"source": "seed", "topic": "אבחון MDT,Manitou Diag", "equipment": "MLT630,MLT741,MT1840,MT2150", "symptom": "קודי שגיאה,אבחון", "brand": "Manitou"}
    },
    {
        "id": "manitou_transmission_zf_005",
        "text": (
            "תיבת הילוכים ZF במאניטו MLT/MT - תקלות שידור\n\n"
            "טלסקופי מאניטו מצוידים בתיבות הילוכים ZF Powershift (4WG-98 / 4WG-155).\n"
            "4 הילוכים קדימה + 3 אחורה, הנעה 4x4 קבועה.\n\n"
            "1. תיבת הילוכים לא מחלפת (Transmission Won't Shift)\n"
            "   קוד: Fault 0031 = Transmission Pressure Low.\n"
            "   לחץ Clutch תקין ZF: 14–18 בר.\n"
            "   גורם: שמן גיר נמוך, או Clutch Pack שחוק.\n"
            "   בדיקה: מד לחץ על Test Port P (ליד תיבת הגיר).\n"
            "   שמן מאושר: ZF Lifeguard Fluid 6 (ATF).\n\n"
            "2. 'בהלה' (Hunting) בין הילוכים 2 ל-3\n"
            "   גורם: Shift Solenoid ב-ZF לא מגיב בזמן.\n"
            "   קוד: ZF Fault E10 = Shift Valve Response Slow.\n"
            "   פתרון: החלף שמן גיר ופילטר, אם לא עוזר — החלף Solenoid.\n\n"
            "3. כלי לא נוסע קדימה (No Forward Drive)\n"
            "   בדוק: מנוף FNR (Forward-Neutral-Reverse) — קוד Fault 0042 = Selector Signal Lost.\n"
            "   גורם: מגע מנוף FNR פגום, או חיבור חשמלי רופף.\n"
            "   פתרון: בדוק Connector Transmission TCU, מדוד אות FNR.\n\n"
            "4. Axle Lock (נעילת ציר) לא פועלת\n"
            "   מאניטו MLT עם Axle Lock (נעילת ציר אחורי לייצוב).\n"
            "   גורם: Axle Lock Solenoid פגום, קוד: Fault 0042.\n"
            "   בדיקה: MDT → Active Check → Rear Axle Lock Solenoid.\n\n"
            "5. Parking Brake לא משתחרר\n"
            "   מאניטו: Parking Brake ספרינגי, נשחרר בלחץ הידראולי.\n"
            "   גורם: Brake Release Solenoid פגום, או לחץ Pilot נמוך (< 25 בר).\n"
            "   פתרון: בדוק Solenoid, בדוק לחץ Pilot System."
        ),
        "metadata": {"source": "seed", "topic": "תיבת הילוכים ZF,שידור", "equipment": "MLT630,MLT741,MLT845,MT1840", "symptom": "לא מחלף הילוך,לא נוסע,נעילת ציר", "brand": "Manitou"}
    },
    {
        "id": "manitou_lmi_safety_006",
        "text": (
            "מערכת LMI — Load Moment Indicator (מחשב עומסים) מאניטו\n\n"
            "ה-LMI (Load Moment Indicator) הוא מחשב הגנת עומסים חובה בטלסקופי מאניטו.\n"
            "המערכת מחשבת את רגע ההרמה בזמן אמת ועוצרת תנועות מסוכנות.\n\n"
            "1. LMI נכנסת ל-Alarm ועוצרת את הזרוע\n"
            "   תסמין: נורת אדומה + עצירה בתנועה.\n"
            "   גורם א: עומס בפועל גדול מהמותר — בדוק Load Chart.\n"
            "   גורם ב: כיול LMI שגוי — מאמין שהכלי נטוי מדי.\n"
            "   בדיקה: MDT → LMI Calibration → כייל מחדש.\n\n"
            "2. LMI מציגה ערכים שגויים\n"
            "   גורם: חיישן עומס (Load Cell) ב-Lifting Hook פגום.\n"
            "   קוד: Fault 0021 = Load Cell Signal Error.\n"
            "   פתרון: החלף Load Cell.\n\n"
            "3. חיישן זווית זרוע (Boom Angle Sensor) שגוי\n"
            "   LMI מסתמך על זווית זרוע מדויקת לחישוב רגע.\n"
            "   קוד: Fault 0023 = Boom Angle Signal Out of Range.\n"
            "   כיול: MDT → Sensor Calibration → Boom Angle:\n"
            "   a. הנח Boom אופקי (0°), לחץ 'Set Zero'.\n"
            "   b. הרם Boom לזווית מקסימום, לחץ 'Set Max'.\n\n"
            "4. ביטול LMI זמני (Override) — מתי מותר?\n"
            "   מאניטו מאפשרת Override זמני לצורך עבודת תחזוקה בלבד.\n"
            "   אסור להשתמש ב-Override בעבודה רגילה — סכנת נפגשות!\n"
            "   Override: לחץ ממושך על כפתור LMI + כפתור הזרוע."
        ),
        "metadata": {"source": "seed", "topic": "LMI,מחשב עומסים,בטיחות", "equipment": "MLT630,MLT741,MT1840,MT2150", "symptom": "LMI עוצרת תנועה,ערכים שגויים", "brand": "Manitou"}
    },
    {
        "id": "manitou_maintenance_mlt741_007",
        "text": (
            "לוח תחזוקה טלסקופ מאניטו MLT741 - לפי שעות\n\n"
            "תחזוקה יומית:\n"
            "- בדוק מפלס שמן מנוע Deutz TCD 4.1\n"
            "- בדוק מפלס נוזל קירור (בין MIN ל-MAX)\n"
            "- בדוק מפלס שמן הידראולי — Sight Glass על מיכל\n"
            "- בדוק רמת נוזל קירור בנגד קפאון (Anti-freeze) בחורף\n"
            "- שמן נקבי גריז: Boom Pivot Pin + Lift Cylinder Pins (4 נקבים)\n\n"
            "כל 250 שעות:\n"
            "- החלף שמן מנוע Deutz (10W-40 ACEA E6, 8 ליטר) + פילטר שמן\n"
            "- החלף מסנן דלק ראשי ומשני\n"
            "- שמן נקבי גריז: זרוע, Tilt Cylinder, Carriage Pins\n\n"
            "כל 500 שעות:\n"
            "- החלף פילטר Return Line הידראולי\n"
            "- בדוק ורענן שמן Transmission ZF (ZF Lifeguard Fluid 6)\n"
            "- בדוק LMI Calibration — ביצוע בדיקת כיול\n"
            "- בדוק מצב Slide Pads בזרוע — עובי מינימלי 3 מ\"מ\n\n"
            "כל 1000 שעות:\n"
            "- החלף שמן Transmission ZF + פילטר גיר\n"
            "- בדוק ורענן שמן גשרים קדמי ואחורי (SAE 90 GL-5)\n"
            "- בדוק מצב שרשרות ארכה Boom — מתיחה ושחיקה\n"
            "- בדוק מצב Brake Pads\n\n"
            "כל 2000 שעות:\n"
            "- החלף שמן הידראולי מלא (46 VG Hydraulic Oil, 80 ליטר)\n"
            "- החלף שמן גשרים קדמי ואחורי\n"
            "- בדוק EGR Valve ו-DPF — נקה אם נדרש"
        ),
        "metadata": {"source": "seed", "topic": "תחזוקה מניעתית", "equipment": "MLT741,MLT630,MLT845", "symptom": "תחזוקה", "brand": "Manitou"}
    },
]

added = 0
for entry in ENTRIES:
    rag.add_document(entry["text"], entry["metadata"], entry["id"])
    added += 1
    print(f"  + {entry['id']}")

print(f"\nAdded {added} Manitou entries. Total KB: {rag.count()} chunks")
