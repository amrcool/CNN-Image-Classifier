from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
import cv2

app = FastAPI()

# Load the model
loaded_model = tf.keras.models.load_model('cnn_model.keras')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read and process the image file
    image_data = await file.read()
    testing_image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Preprocess the image
    gray_image = cv2.cvtColor(testing_image, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY_INV)
    resized_image = cv2.resize(im, (28, 28))
    reshaped_image = resized_image.reshape(-1, 28, 28, 1)
    arr_image = np.array(reshaped_image, dtype='float32')
    
    # Make a prediction
    prediction = loaded_model.predict(arr_image)
    predicted_class = int(np.argmax(prediction))
    
    return JSONResponse(content={'predicted_class': predicted_class})
