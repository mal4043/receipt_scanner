import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="סורק קבלות יציב", layout="centered")

st.title("📋 סורק קבלות - גרסה יציבה")
st.write("העלה תמונה והטקסט יופיע למטה בתיבה הניתנת להעתקה.")

uploaded_file = st.file_uploader("בחר תמונת קבלה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה המקורית', use_container_width=True)
    
    with st.spinner('מחלץ טקסט...'):
        try:
            # חילוץ טקסט בעברית ובאנגלית
            text = pytesseract.image_to_string(image, lang='heb+eng')
            
            if text.strip():
                st.success("הטקסט חולץ בהצלחה!")
                # תיבה להעתקה מהירה
                st.subheader("סמן והעתק מכאן:")
                st.text_area(label="תוצאה:", value=text, height=400)
                
                # כפתור הורדה
                st.download_button("הורד כקובץ TXT", text)
            else:
                st.warning("לא זוהה טקסט ברור בתמונה.")
        except Exception as e:
            st.error(f"שגיאה בעיבוד: {e}")
            st.info("ודא שיצרת קובץ בשם packages.txt עם התוכן המתאים.")

else:
    st.info("ממתין לקובץ...")
