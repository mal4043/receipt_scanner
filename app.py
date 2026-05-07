import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.set_page_config(page_title="סורק קבלות להעתקה")

st.title("📋 סורק קבלות להעתקה מהירה")
st.write("העלה תמונה והטקסט יופיע בתיבה עם כפתור העתקה.")

uploaded_file = st.file_uploader("בחר תמונה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה המקורית', use_container_width=True)
    
    with st.spinner('ה-AI מנתח... (בפעם הראשונה זה לוקח זמן, אל תסגור)'):
        try:
            # המרת התמונה
            img_array = np.array(image)
            
            # טעינת המודל - הוספתי הגנה למקרה שעברית נכשלת
            try:
                reader = easyocr.Reader(['he', 'en'], gpu=False)
            except:
                reader = easyocr.Reader(['en'], gpu=False)
                st.warning("עובד במצב אנגלית בלבד עקב תקלה זמנית בשפה העברית.")

            result = reader.readtext(img_array, detail=0)
            
            if result:
                full_text = "\n".join(result)
                
                st.subheader("תוצאה להעתקה (לחץ על האייקון מצד ימין):")
                # השימוש ב-st.code נותן כפתור העתקה מובנה!
                st.code(full_text, language="text")
                
                st.download_button("הורד כקובץ TXT", full_text)
            else:
                st.warning("לא זוהה טקסט.")
                
        except Exception as e:
            st.error(f"שגיאה בתהליך: {e}")
