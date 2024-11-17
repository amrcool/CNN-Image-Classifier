

# 🌟 CNN Image Classifier 🌟  

This project implements a **Convolutional Neural Network (CNN)** image classifier using:  
🚀 **FastAPI** backend for serving predictions.  
🖼️ Users can upload images, and the application predicts the class label for each image utilizing a pre-trained model.  

---

## ✨ Features  

✔️ **Deep Learning Model**: A CNN model trained on an image dataset for accurate classification.  
✔️ **FastAPI Backend**: Provides a RESTful API endpoint for image prediction.  
✔️ **Streamlit Frontend**: User-friendly interface for real-time image uploads and predictions.  

---

## 🐳 Using Docker  

If you prefer to use Docker for the backend, follow these steps:  

### Pull the Docker Image  
```bash  
docker pull amrcool/cnn_backend  
```  

### Run the Docker Container  
```bash  
docker run -p 8000:8000 amrcool/cnn_backend  
```  
This will start the FastAPI server on `http://localhost:8000`.  

> **Note**: The Docker image provided is for the **backend** only. You can integrate it with any frontend of your choice (e.g., Streamlit, React, etc.) to build a complete application.  

For more details on the Docker image, visit the [Docker Hub repository](https://hub.docker.com/r/amrcool/cnn_backend).  

---

## ⚙️ Setup and Installation (Local Setup)

To run the backend and frontend locally, follow these steps:

### 1️⃣ Clone the Repository  
```bash  
git clone https://github.com/amrcool/cnn-image-classifier.git  
cd cnn-image-classifier  
```  

### 2️⃣ Install Dependencies  
Create a virtual environment and install the required dependencies:  
```bash  
python -m venv .myenv  
source .myenv/bin/activate  # On Windows, use .myenv\Scripts\activate  
pip install -r requirements.txt  
```  

### 3️⃣ Prepare the Model  
Save your trained CNN model in the project directory as `cnn_model.keras`.  
You can replace this with your own trained model if necessary.  

### 4️⃣ Start the FastAPI Server  
In the project directory, run the FastAPI server using Uvicorn:  
```bash  
uvicorn server:app --reload  
```  
The server will be available at `http://127.0.0.1:8000`.  

### 5️⃣ Run the Streamlit Frontend  
In a new terminal window, run the Streamlit app:  
```bash  
streamlit run app.py  
```  
This will start the Streamlit app on `http://localhost:8501`.  

---

## 🎯 Usage  

1. Open your web browser and navigate to the Streamlit interface at `http://localhost:8501`.  
2. Upload an image in JPG, JPEG, or PNG format.  
3. The app will display the uploaded image along with the predicted class label.  

---

## 📚 API Reference  

### POST `/predict`  

- **Description**: Accepts an image file and returns the predicted class.  
- **Request**: Multipart form-data with the image file under the key `file`.  
- **Response**: A JSON object containing the `predicted_class`.  

### Example Request (using `curl`):  
```bash  
curl -X 'POST' \  
  'http://127.0.0.1:8000/predict' \  
  -H 'accept: application/json' \  
  -H 'Content-Type: multipart/form-data' \  
  -F 'file=@your_image.jpg'  
```  

### Example Response:  
```json  
{  
  "predicted_class": 3  
}  
```  

---

## 💡 Notes  

- Ensure the **FastAPI server** is running before sending requests to the `/predict` endpoint.  
- If you want to use your own trained model, save it as a `.keras` file and place it in the project directory.  
- The Docker image is only for the **backend**; you can connect it with any frontend framework you prefer.  

---

## 📦 Example  

Run the **FastAPI server** and the **Streamlit frontend** locally, upload an image via the Streamlit UI, and observe the classification results!  
