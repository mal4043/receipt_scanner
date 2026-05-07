import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("סורק קבלות חכם 📄")
st.write("העלה תמונה של קבלה וה-AI יחלץ את הטקסט")

# העלאת קובץ
uploaded_file = st.file_uploader("בחר תמונת קבלה...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # הצגת התמונה
    image = Image.open(uploaded_file)
    st.image(image, caption='הקבלה שהועלתה', use_column_width=True)
    
    with st.spinner('מנתח את הקבלה...'):
        # המרת התמונה לפורמט שהספריה מבינה
        img_array = np.array(image)
        
        # הפעלת ה-OCR (תומך בעברית ואנגלית)
        reader = easyocr.Reader(['he', 'en'])
        result = reader.readtext(img_array, detail=0)
        
        # הצגת התוצאות
        st.subheader("הטקסט שזוהה:")
        full_text = "\n".join(result)
        st.text_area("תוצאה:", full_text, height=300)
        
        # כפתור הורדה כקובץ טקסט
        st.download_button("הורד כקובץ TXT", full_text, file_name="receipt.txt")
