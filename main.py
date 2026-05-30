import tkinter as tk
from tkinter import messagebox
import math

# دالة حساب الجذر التربيعي
def calculate_square_root():
    try:
        # الحصول على القيمة المدخلة وتحويلها إلى رقم
        entry_value = entry.get()
        
        # التأكد من أن المدخل عدد صحيح وطبيعي
        if not entry_value.isdigit():
            raise ValueError("الرجاء إدخال عدد طبيعي صحيح فقط (أكبر من أو يساوي 0).")
        
        number = int(entry_value)
        
        # حساب الجذر التربيعي
        result = math.sqrt(number)
        
        # عرض النتيجة (إذا كانت النتيجة فاصلة صفرية، نعرضها كعدد صحيح)
        if result.is_integer():
            label_result.config(text=f"الجذر التربيعي هو: {int(result)}", fg="green")
        else:
            label_result.config(text=f"الجذر التربيعي هو: {result:.4f}", fg="green")
            
    except ValueError as e:
        # عرض رسالة خطأ في حال إدخال نص أو عدد سالب
        messagebox.showerror("خطأ في الإدخال", str(e))

# إنشاء نافذة التطبيق الرئيسية
window = tk.Tk()
window.title("برنامج حساب الجذر الطبيعي")
window.geometry("350x250")
window.configure(bg="#f0f0f0")

# عنوان التطبيق داخل النافذة
label_title = tk.Label(window, text="حساب الجذر التربيعي لعدد طبيعي", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_title.pack(pady=15)

# صندوق إدخال الرقم
entry = tk.Entry(window, font=("Arial", 12), justify="center", width=20)
entry.pack(pady=10)
entry.insert(0, "أدخل العدد هنا") # نص توضيحي

# زر الحساب
btn_calculate = tk.Button(window, text="احسب الجذر", font=("Arial", 12), bg="#4CAF50", fg="white", command=calculate_square_root)
btn_calculate.pack(pady=10)

# مكان عرض النتيجة
label_result = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_result.pack(pady=15)

# تشغيل النافذة
window.mainloop()