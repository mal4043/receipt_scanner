import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="סורק קבלות להעתקה")

st.title("📋 סורק קבלות להעתקה מהירה")
st.write("העלה תמונה והטקסט יופיע בתיבה למטה.")

uploaded_file = st.file_uploader("בחר תמונה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה המקורית', use_container_width=True)
    
    with st.spinner('מנתח טקסט (זה עשוי לקחת חצי דקה בפעם הראשונה)...'):
        try:
            # המרת התמונה לפורמט מתאים
            img_array = np.array(image)
            
            # הפעלת ה-OCR - נשתמש באנגלית כברירת מחדל אם עברית נכשלת
            reader = easyocr.Reader(['en', 'he'])
            result = reader.readtext(img_array, detail=0)
            
            if result:
                st.success("הטקסט מוכן!")
                
                # חיבור כל השורות לטקסט אחד ארוך
                full_text = "\n".join(result)
                
                # --- החלק החשוב: תיבה להעתקה ---
                st.subheader("סמן והעתק את הטקסט מכאן:")
                st.text_area(label="תוצאה:", value=full_text, height=400)
                
                st.download_button("הורד כקובץ טקסט", full_text)
            else:
                st.warning("לא נמצא טקסט בתמונה.")
                
        except Exception as e:
            st.error(f"שגיאה: {e}")
            st.info("נסה לרענן את הדף או להעלות תמונה ברורה יותר.")

else:
    st.info("אנא העלה קובץ כדי להתחיל.")
