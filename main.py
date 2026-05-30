import streamlit as st
import math

# إعدادات واجهة التطبيق لتناسب الهواتف
st.set_page_config(page_title="حساب الجذر التربيعي", page_icon="🧮", layout="centered")

# عنوان التطبيق الرئيسي
st.title("🧮 تطبيق حساب الجذر التربيعي")
st.write("أدخل أي عدد طبيعي لمعرفة جذره التربيعي فوراً!")

# صندوق إدخال الرقم (سهل اللمس والاستخدام على الجوال)
number = st.number_input("أدخل العدد هنا:", min_value=0, step=1, value=0)

# زر الحساب
if st.button("احسب الآن ✨"):
    if number >= 0:
        result = math.sqrt(number)
        # عرض النتيجة بلون أخضر مريح
        st.success(f"💡 الجذر التربيعي للعدد **{number}** هو:  **{result:.4f}**")
    else:
        st.error("الرجاء إدخل عدد طبيعي صحيح.")
