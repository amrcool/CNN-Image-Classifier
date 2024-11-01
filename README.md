---

# CNN Image Classifier

This project implements a Convolutional Neural Network (CNN) image classifier using a FastAPI backend for serving predictions and a Streamlit frontend for an intuitive user experience. Users can upload images, and the application predicts the class label for each image utilizing a pre-trained model.

## Features

- **Deep Learning Model**: A CNN model trained on a comprehensive image dataset for accurate classification.
- **FastAPI Backend**: Offers a RESTful API endpoint for efficient image prediction.
- **Streamlit Frontend**: Provides a user-friendly interface for real-time image uploads and predictions.

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
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Model**: Save your trained CNN model in the project directory or specify its path in `app.py`.

4. **Start the FastAPI Server**:
   ```bash
   uvicorn app:app --reload
   ```

5. **Run the Streamlit App**:
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. Open your web browser and navigate to the Streamlit interface at `http://localhost:8501`.
2. Upload an image in JPG, JPEG, or PNG format.
3. The app will display the uploaded image along with the predicted class label.

## API Reference

### POST `/predict`

- **Description**: Accepts an image file and returns the predicted class.
- **Request**: Multipart form-data with the image file under the key `file`.
- **Response**: A JSON object containing the `predicted_class`.

## Example

Run both the FastAPI and Streamlit servers, upload an image through the Streamlit UI, and observe the classification results.


---
