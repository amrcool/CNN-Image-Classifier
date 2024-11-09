---

# CNN Image Classifier

This project implements a Convolutional Neural Network (CNN) image classifier using a FastAPI backend for serving predictions and a Streamlit frontend for an intuitive user experience. Users can upload images, and the application predicts the class label for each image utilizing a pre-trained model.

## Features

- **Deep Learning Model**: A CNN model trained on an image dataset for accurate classification.
- **FastAPI Backend**: Provides a RESTful API endpoint for image prediction.
- **Streamlit Frontend**: A user-friendly interface for real-time image uploads and predictions.

## Requirements

To run this project, you need the following:

- Python 3.8+
- TensorFlow
- OpenCV
- FastAPI
- Uvicorn
- Streamlit
- Requests

## Setup and Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amrcool/cnn-image-classifier.git
   cd cnn-image-classifier
   ```

2. **Install the Dependencies**:
   Create a virtual environment and install the required dependencies:
   ```bash
   python -m venv .myenv
   source .myenv/bin/activate  # On Windows, use .myenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Prepare the Model**:
   Save your trained CNN model in the project directory as `cnn_model.keras`. You can replace this with your own trained model if necessary.

4. **Start the FastAPI Server**:
   In the project directory, run the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
   This will start the FastAPI server on `http://127.0.0.1:8000`.

5. **Run the Streamlit App**:
   In a new terminal window, run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   This will start the Streamlit app on `http://localhost:8501`.

## Usage

1. Open your web browser and navigate to the Streamlit interface at `http://localhost:8501`.
2. Upload an image in JPG, JPEG, or PNG format.
3. The app will display the uploaded image along with the predicted class label.

## API Reference

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

## Notes

- Make sure the FastAPI server is running before using the Streamlit app, as Streamlit will communicate with the FastAPI server to get predictions.
- If you need to use your own trained model, ensure it is saved as a `.keras` file and placed in the project directory.

## Example

Run both the FastAPI and Streamlit servers, upload an image through the Streamlit UI, and observe the classification results.

---
