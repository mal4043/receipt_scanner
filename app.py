import streamlit as st
import google.generativeai as genai
from PIL import Image

# הגדרת ה-API KEY (מומלץ לאחסן את המפתח ב-Secrets של Streamlit)
API_KEY = "AIzaSyCuKx7oRY9G1pIzy8wV9yU7xuDvAJ90vXY"
genai.configure(api_key=API_KEY)

st.title("סורק קבלות חכם 🤖")

uploaded_file = st.file_uploader("העלה קבלה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה שהועלתה', use_container_width=True)
    
    if st.button("חלץ נתונים"):
        with st.spinner('ה-AI מנתח את הקבלה...'):
            try:
                # הגדרת המודל
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # ההנחיה (Prompt) - כאן אתה קובע מה אתה רוצה לקבל
                prompt = """
                תנתח את תמונת הקבלה הזו ותחזיר לי רק את הפרטים הבאים בטקסט נקי:
                1. שם העסק
                2. תאריך
                3. סכום כולל לתשלום
                4. מספר ח"פ (אם מופיע)
                """
                
                response = model.generate_content([prompt, image])
                
                st.success("הנתונים חולצו:")
                # תיבת טקסט שניתן להעתיק ממנה
                st.text_area("נתוני הקבלה:", response.text, height=200)
                
            except Exception as e:
                st.error(f"שגיאה: {e}")

# הערה: מחק את קובץ packages.txt אם יצרת אותו, הוא לא נחוץ יותר
