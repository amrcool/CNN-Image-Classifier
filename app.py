import streamlit as st
import requests
import numpy as np
import cv2

st.title('CNN Image Classifier')

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

def predict_image_class(image_bytes):
    # Send the raw image bytes to the FastAPI server
    files = {'file': image_bytes}
    response = requests.post("http://127.0.0.1:8000/predict", files=files)

    # Check for successful response
    if response.status_code == 200:
        predicted_class = response.json().get('predicted_class')
        return predicted_class
    else:
        st.error("Error: Could not get a valid response from the server.")
        return None

if uploaded_file is not None:
    # Convert uploaded file to image array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    class_names = ['T_shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    # Send the raw image bytes to the server
    uploaded_file.seek(0)  # Reset file pointer after reading for OpenCV
    predicted_class = predict_image_class(uploaded_file)

    if predicted_class is not None:
        st.write(f"Predicted Class: {class_names[predicted_class]}")
