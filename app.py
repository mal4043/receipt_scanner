import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# הגדרת כותרת האפליקציה
st.set_page_config(page_title="סורק קבלות AI", layout="centered")

st.title("📄 סורק קבלות חכם למנהל חשבונות")
st.write("העלה תמונה של קבלה והמערכת תחלץ את הטקסט באופן אוטומטי.")

# כפתור להעלאת קובץ
uploaded_file = st.file_uploader("בחר תמונת קבלה (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. הצגת התמונה שהועלתה
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה שהועלתה', use_column_width=True)
    
    st.write("---")
    
    # 2. תחילת תהליך ה-AI
    with st.spinner('ה-AI מנתח את הטקסט... זה יכול לקחת כמה שניות...'):
        try:
            # המרת התמונה לפורמט עבודה של ה-AI
            img_array = np.array(image)
            
            # הגדרת ה-OCR לקריאת עברית ואנגלית
            reader = easyocr.Reader(['he', 'en'])
            
            # ביצוע הקריאה בפועל
            result = reader.readtext(img_array, detail=0)
            
            # 3. הצגת התוצאות למשתמש
            if result:
                st.success("✅ הטקסט חולץ בהצלחה!")
                st.subheader("הטקסט שנמצא:")
                
                # הדפסת כל שורה שנמצאה
                for line in result:
                    st.write(f"🔹 {line}")
                
                # כפתור להורדת כל הטקסט כקובץ
                full_text = "\n".join(result)
                st.download_button(
                    label="הורד את הטקסט כקובץ TXT",
                    data=full_text,
                    file_name="receipt_data.txt",
                    mime="text/plain"
                )
            else:
                st.warning("לא הצלחתי לזהות טקסט בתמונה. נסה לצלם ממרחק קרוב יותר או בתאורה טובה יותר.")
                
        except Exception as e:
            st.error(f"אירעה שגיאה בעיבוד התמונה: {e}")

else:
    st.info("ממתין להעלאת קבלה...")
