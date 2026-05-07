import streamlit as st
from PIL import Imaga
import pytesseract

# כותרת
st.title("סורק קבלות - העתקת טקסט 📋")

# העלאת תמונה
uploaded_file = st.file_uploader("העלה קבלה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה', use_column_width=True)
    
    with st.spinner('מחלץ טקסט...'):
        # חילוץ הטקסט (תומך בעברית ואנגלית)
        # הערה: בשרתים מסוימים יש להתקין חבילת שפה, כאן זה ינסה לקרוא מה שיש
        try:
            text = pytesseract.image_to_string(image, lang='heb+eng')
        except:
            text = pytesseract.image_to_string(image, lang='eng')

        if text.strip():
            st.subheader("הטקסט שחולץ (ניתן להעתקה):")
            # יצירת תיבת טקסט שניתן לסמן ולהעתיק ממנה
            st.text_area("סמן והעתק מכאן:", text, height=300)
            
            # כפתור הורדה כבונוס
            st.download_button("הורד כקובץ טקסט", text)
        else:
            st.warning("לא זוהה טקסט בתמונה.")
