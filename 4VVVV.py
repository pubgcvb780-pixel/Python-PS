import os
import requests
import time

# ================= COLORS (NEON) =================
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[38;5;196m'
GREEN = '\033[38;5;46m'
YELLOW = '\033[38;5;226m'
CYAN = '\033[38;5;51m'
PURPLE = '\033[38;5;201m'
WHITE = '\033[38;5;15m'
ORANGE = '\033[38;5;208m'

# ================= TOOLS BY CATEGORY =================
TOOLS = {
    "1": {
        "name": "قسم الادوات الصيد ",
        "tools": {
            "1": ("ادات صيد حسابات تيك توك مدفوعة", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20%D9%85%D8%AA%D8%A7%D8%AD.py"),
            "2": ("ادات صيد حسابات سافيوم", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B3%D8%A7%D9%81%D9%8A%D9%88%D9%85.py"),
            "3": ("صيد حسابات فيس بوك مدغوعة باسور و (ايميل او رقم )", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B5%D9%8A%D8%AF%20%D8%AD%D8%B3%D8%A7%D8%A8%D8%A7%D8%AA%20%D9%81%D9%8A%D8%B3%20%D8%A8%D9%88%D9%83%20%D8%A8%D8%A7%D8%B3%D9%88%D8%B1%D8%AF%20.py"),
            "4": ("ادات صيد حسابات فيس بوك متاح", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D9%81%D9%8A%D8%B3%20%D8%A8%D9%88%D9%83%20%D9%85%D8%AA%D8%A7%D8%AD%20.py"),
            "5": ("ادات صيد حسابات تويتر متاح", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D9%85%D8%AA%D8%A7%D8%AD%D8%A7%D8%AA%20%D8%AA%D9%88%D9%8A%D8%AA%D8%B1%20.py"),
            "6": ("ادات صيد يوزرات (تيك توك وتلجرام وانستكرام) مدفوعة", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D9%8A%D9%88%D8%B2%D8%B1%D8%A7%D8%AA10$$%20(1)%F0%9F%91%BF.py"),
            "7": ("ادات صيد متاح انستكرام  2K", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%F0%9F%91%BF%D8%A7%D9%86%D8%B3%D8%AA%D9%83%D8%B1%D8%A7%D9%85%20%D8%AC%D9%8A%D8%AA%20%D9%87%D8%A7%D8%A8.py"),
            "8": ("صيد حسابات بلياردو", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/PLPL8.py"),
            "9": ("صيد حسابات انستكرام 2010_2012", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/hotmail%202010-12.py"),
            "10": ("صيد حسابات  انستكرام 5انواع", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B5%D9%8A%D8%AF%20%D8%AD%D8%B3%D8%A7%D8%A8%D8%A7%D8%AA%20%D8%A7%D9%86%D8%B3%D8%AA%D9%83%D8%B1%D8%A7%D9%85%205%D9%86%D9%88%D8%B9.py"),
            "11": ("صيد حسابات كارباركينج", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B5%D9%8A%D8%AF%20%D8%AD%D8%B3%D8%A7%D8%A8%D8%A7%D8%AA%20%D9%83%D8%A7%D8%B1%20%D8%A8%D8%A7%D8%B1%D9%83%D9%8A%D9%86%D8%AC%201.py"),
        }
    },
    "2": {
        "name": "قسم ادوات البلاغ ",
        "tools": {
            "1": ("ادات بلاغات فيس بوك  حقيقي", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/Facebook%20.py"),
            "2": ("اداة بلاغات انستكرام  حقيقي", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%A8%D9%84%D8%A7%D8%BA%D8%A7%D8%AA%20%D8%A7%D9%86%D8%B3%D8%AA%D8%B7%D8%B1%D8%A7%D9%85%202.py"),
            "3": ("ادات بلاغات انستكرام حقيقي النسخه الاولة", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%A8%D9%84%D8%A7%D8%BA%D8%A7%D8%AA%20%D8%A7%D9%86%D8%B3%D8%AA%D9%83%D8%B1%D8%A7%D9%85%20%D8%AD%D9%82%D9%8A%D9%82%D9%8A%20%20%F0%9F%91%BF.py"),
            "4": ("(بوت) بلاغات تلجرام  حقيقي شد خارجي وداخلي", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%A8%D9%84%D8%A7%D8%BA%D8%A7%D8%AA%20%D8%AA%D9%84%D8%AC%D8%B1%D8%A7%D9%85%20%D8%B4%D8%AF%20%D8%AE%D8%A7%D8%B1%D8%AC%D9%8A%20%D9%88%D8%AF%D8%A7%D8%AE%D9%84%D9%8A(%D8%A8%D9%88%D8%AA)%20.py"),
            "5": ("ادات بلاغات تيك توك حقيقي مدفوعة", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%A8%D9%84%D8%A7%D8%BA%D8%A7%D8%AA%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20%D8%AD%D9%82%D9%8A%D9%82%D9%8A%20%20.py"),
            "6": ("ادات الهجوم علا المواقع (تعطيل)", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%A7%D9%8A%D9%82%D8%A7%D9%81%20%D8%A7%D9%84%D9%85%D9%88%D8%A7%D9%82%D8%B9%20.py"),
        }
    },
    "3": {
        "name": "قسم ادوات الرشق ",
        "tools": {
            "1": ("ادات تعاليق تيك توك(رشق)", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AA%D8%B9%D8%A7%D9%84%D9%8A%D9%82%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20(%D8%B1%D8%B4%D9%82).py"),
            "2": ("ادات رشق متابعين تيك توك من سيشنات", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B1%D8%B4%D9%80%D9%80%D9%82%20%D9%85%D8%AA%D8%A7%D8%A8%D8%B9%D9%80%D9%80%D9%80%D9%8A%D9%86%20%D8%AA%D9%80%D9%80%D9%80%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20%F0%9F%91%BF.py"),
            "3": ("ادات رشق تيك توك من موقع", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B1%D8%B4%D9%82%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20.py"),
            "4": ("ادات رشق مشاهدات تيك توك لانهائي", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B1%D8%B4%D9%82%20%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A7%D8%AA%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83.py"),
        }
    },
    "4": {
        "name": "قسم الخدمات المتوفره",
        "tools": {
            "1": ("(بوت) سحب لسته تيك توك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%20%D8%B3%D8%AD%D8%A8%20%D9%84%D8%B3%D8%AA%D9%87%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83.%F0%9F%91%BF.py"),
            "2": ("توصيل ريست انستكرام", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/Reset.py"),
            "3": ("ادات حذف حساب تيك توك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AA%D8%AA%D8%B7%D9%8A%D8%B1%20%D8%A7%D9%84%D8%AD%D8%B3%D8%A7%D8%A8.py"),
            "4": ("ادات تحميل فيدوهات من تيك توك 8K", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AA%D8%AD%D9%80%D9%85%D9%8A%D9%84%204K%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20%F0%9D%91%B7%F0%9D%91%BA%20(%D8%A8%D9%88%D8%AA).py"),
            "5": ("ادات تغيير يوزر حساب التيك توك للضحية", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AA%D8%BA%D9%8A%D9%8A%D8%B1%D9%88%20%D9%8A%D9%88%D8%B2%D8%B1%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20.py"),
            "6": ("ادات حذف منشورات الضحية تيك توك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AD%D8%B0%D9%81%20%D9%81%D9%8A%D8%AF%D9%88%D9%87%D8%A7%D8%AA%20%D8%A7%D9%84%D8%AD%D8%B3%D8%A7%D8%A8.py"),
            "7": ("ادات حضر اصدقاء الضحيه تيك توك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AD%D8%B6%D8%B1%20%D8%B9%D9%86%20%D8%B7%D8%B1%D9%8A%D9%82%20%D8%B3%D9%8A%D8%B4%D9%86%20.py"),
            "8": ("(بوت)خدمات تيك توك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%AE%D8%AF%D9%85%D8%A7%D8%AA%20%D8%AA%D9%8A%D9%83%20%D8%AA%D9%88%D9%83%20%D8%A8%D9%88%D8%AA%20(%D8%A8%D9%88%D8%AA).py"),
            "9": ("ادات سحب ابروكسي مدفوع", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B3%D8%AD%D8%A8%20%D8%A8%D8%B1%D9%88%D9%83%D8%B3%D9%8A.py"),
            "10": ("ادات استخراج سيشن انستكرام", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B3%D8%AD%D8%A8%20%D8%B3%D9%8A%D8%B4%D9%86%20%D8%A7%D9%86%D8%B3%D8%AA%D9%83%D8%B1%D8%A7%D9%85%20.py"),
            "11": ("(بوت) سحب سيشنات تيك توك لانهائي", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D8%B3%D8%AD%D8%A8%20%D8%B3%D9%8A%D8%B4%D9%86%D8%A7%D8%AA%20%D8%B9%D8%B4%D9%88%D8%A7%D8%A6%D9%8A%20(%D8%A8%D9%88%D8%AA).py"),
            "12": ("ادات فحص سيشنات تيك توك سريعة جدا", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D9%81%D8%AD%D8%B5%20%D8%B3%D9%8A%D8%B4%D9%86%D8%A7%D8%AA.py"),
            "13": ("تحميل كل مكاتب بايثون", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%F0%9D%90%8F%F0%9D%90%88%F0%9D%90%8F%20%F0%9D%90%81%F0%9D%90%98%20PS%20.py"),
            "14": ("فحص IP هاتفك", "https://github.com/pubgcvb780-pixel/Power/raw/refs/heads/main/%D9%81%D8%AD%D8%B5ip.py"),
        }
    }
}

# ================= PRINT FUNCTION =================
def p(text, color=WHITE, delay=0):
    print(f"{color}{BOLD}{text}{RESET}")
    if delay:
        time.sleep(delay)

# ================= SURAH + VIRTUES =================
def surah_and_virtues():
    p("سورة الكوثر", CYAN, 0.6)
    p("إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ", WHITE, 0.6)
    p("فَصَلِّ لِرَبِّكَ وَانْحَرْ", WHITE, 0.6)
    p("إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ", WHITE, 0.8)
    print()
    
    virtues = [  
        "وُلِدَ الإمام علي (ع) في جوف الكعبة",  
        "أول من آمن برسول الله ﷺ",  
        "قلع باب خيبر بيده",  
        "نام في فراش النبي ليلة الهجرة",  
        "زوج فاطمة الزهراء (ع)",  
        "أبو الحسنين (ع)",  
        "استُشهد وهو ساجد في المحراب",  
    ]  
    
    for v in virtues:  
        p(f"• {v}", GREEN, 1.5)

# ================= TIMER =================
def timer():
    for i in range(1, 101):
        print(f"\r{ORANGE}{BOLD}LOADING : {i}%{RESET}", end="")
        time.sleep(0.03)
    print()

# ================= RUN TOOL FROM URL =================
def run_tool_from_url(url, tool_name):
    try:
        p(f"\n{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", GREEN, 0.5)
        p(f"جاري تشغيل الأداة: {tool_name}", GREEN, 1)
        p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", GREEN, 0.5)
        
        # تحميل الكود من GitHub
        response = requests.get(url)
        if response.status_code == 200:
            # الحصول على الكود
            code = response.text
            
            # حفظ مؤقت في ملف ثم تشغيله
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as tmp:
                tmp.write(code)
                tmp_file = tmp.name
            
            # تشغيل الملف المؤقت
            os.system(f'python "{tmp_file}"')
            
            # حذف الملف المؤقت بعد التشغيل
            os.unlink(tmp_file)
            
            p(f"\n{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", GREEN, 0.5)
            p(f"اكتمل تشغيل الأداة", GREEN, 1)
            p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", GREEN, 0.5)
            
        else:
            p(f"\n{RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)
            p(f"خطأ في تحميل الأداة من الرابط", RED, 1)
            p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)
            
    except Exception as e:
        p(f"\n{RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)
        p(f"حدث خطأ: {str(e)}", RED, 1)
        p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)

# ================= DISPLAY CATEGORIES MENU =================
def show_categories():
    os.system("clear||cls")
    surah_and_virtues()

    # ================= MERGED INFO BOX =================
    p("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓", RED)
    p("┃           ━━━━━━━𝑷𝑺━━━━━━━━━━━━━           ┃", RED)
    p("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫", RED)
    p("┃ WARNING : PAID VIP TOOL                      ┃", RED)
    p("┃ NO SHARE / NO LEAK                           ┃", RED)
    p("┃ PRIVATE USE ONLY                             ┃", RED)

    p("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫", PURPLE)
    p("┃ PS ACCOUNT CREATOR V2.0.0 👿                   ┃", PURPLE)
    p("┃• ADVANCED ANTI-DETECTION SYSTEM               ┃", PURPLE)
    p("┃• PHONE VERIFICATION BYPASS                   ┃", PURPLE)
    p("┃• SMART PROXY INTEGRATION                      ┃", PURPLE)
    p("┃• BEAUTIFUL MODERN INTERFACE                   ┃", PURPLE)
    p("┃• DETAILED STATISTICS                          ┃", PURPLE)
    p("┃• AUTO-SAVE ACCOUNTS                           ┃", PURPLE)
    p("┃• AUTO-RETRY ON FAILURE                        ┃", PURPLE)
    p("┃• LIGHTNING FAST CREATION                     ┃", PURPLE)
    p("┃• 2925 SHADOW HACKER ALL RIGHTS RESERVED       ┃", PURPLE)
    p("┃• WHATSAPP: +9640000000000                      ┃", PURPLE)

    p("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫", GREEN)
    p("┃ DEVELOPER : PS                              ┃", GREEN)
    p("┃ NUMBER    : +9640000000000                  ┃", GREEN)
    p("┃ COUNTRY   : IRAQ THE GREAT                  ┃", GREEN)
    p("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛", RED)

    # ================= DISPLAY MAIN CATEGORIES =================
    p(f"\n{'━' * 45}", CYAN, 0.3)
    p("اختر القسم المطلوب:", YELLOW, 0.3)
    p(f"{'━' * 45}", CYAN, 0.3)
    
    for cat_num, cat_data in TOOLS.items():
        p(f"{'━' * 15}", PURPLE, 0.1)
        p(f"[{cat_num}] {cat_data['name']}", PURPLE, 0.2)
        p(f"{'━' * 45}", PURPLE, 0.1)
    
    p(f"{'━' * 15}", RED, 0.1)
    p(f"[0] للخروج من البرنامج", RED, 0.2)
    p(f"{'━' * 45}", RED, 0.1)

# ================= DISPLAY TOOLS IN CATEGORY =================
def show_tools_in_category(category_key):
    while True:
        os.system("clear||cls")
        selected_category = TOOLS[category_key]
        
        p(f"\n{'━' * 50}", YELLOW, 0.3)
        p(f"{'━' * 50}", YELLOW, 0.3)
        p(f"القسم: {selected_category['name']}", CYAN, 0.3)
        p(f"{'━' * 50}", YELLOW, 0.3)
        p(f"{'━' * 50}", YELLOW, 0.3)
        
        for tool_num, (tool_name, _) in selected_category['tools'].items():
            p(f"{'━' * 20}", GREEN, 0.1)
            p(f"[{tool_num}] {tool_name}", GREEN, 0.15)
            p(f"{'━' * 50}", GREEN, 0.1)
        
        p(f"{'━' * 20}", RED, 0.1)
        p(f"[0] الرجوع للقائمة الرئيسية", RED, 0.2)
        p(f"{'━' * 50}", RED, 0.1)
        
        # Get tool choice
        tool_choice = input(f"\n{CYAN}{BOLD}اختر رقم الأداة => {RESET}").strip()
        
        if tool_choice == "0":
            return  # العودة للقائمة الرئيسية
        
        if tool_choice not in selected_category['tools']:
            p("\nالأداة غير صحيحة!", RED, 1)
            continue
        
        # Get selected tool
        tool_name, tool_url = selected_category['tools'][tool_choice]
        
        # ================= TIMER =================
        timer()
        
        # ================= RUN TOOL DIRECTLY =================
        run_tool_from_url(tool_url, tool_name)
        
        # ================= ASK TO CONTINUE =================
        p(f"\n{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", YELLOW, 0.5)
        back = input(f"{YELLOW}{BOLD}اضغط Enter للرجوع للقائمة أو 0 للخروج: {RESET}").strip()
        p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", YELLOW, 0.5)
        
        if back == "0":
            exit_program()

# ================= EXIT PROGRAM =================
def exit_program():
    p(f"\n{RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)
    p(f"شكراً لاستخدامك الأدوات - تم الخروج", RED, 1)
    p(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", RED, 0.5)
    exit()

# ================= MAIN PROGRAM =================
def main():
    while True:
        show_categories()
        
        # Get category choice
        cat_choice = input(f"\n{CYAN}{BOLD}اختر رقم القسم => {RESET}").strip()
        
        if cat_choice == "0":
            exit_program()
        
        if cat_choice not in TOOLS:
            p("\nالقسم غير صحيح!", RED, 1)
            time.sleep(1)
            continue
        
        show_tools_in_category(cat_choice)

# ================= RUN MAIN PROGRAM =================
if __name__ == "__main__":
    main()