# Symptoms to Diseases Prediction API

## Overview

This project is a Flask-based API designed to predict diseases based on given symptoms using a pre-trained TensorFlow model. It demonstrates the integration of machine learning with web development to provide real-time predictions.

## Complexities

### Model Integration
- **Challenge:** Integrating a TensorFlow model within a Flask API to provide real-time predictions.
- **Solution:** Loaded the pre-trained model using TensorFlow and created prediction endpoints to handle incoming requests and return predictions.

### Data Handling
- **Challenge:** Processing and converting user input into a format suitable for the model.
- **Solution:** Utilized TensorFlow's data processing utilities to convert input text into tensors that the model can understand, ensuring accurate predictions.

## Challenges and Solutions

### Challenge 1: Model Loading
- **Problem:** Efficiently loading a large TensorFlow model on server startup.
- **Solution:** Pre-loaded the model during the Flask app initialization to avoid loading delays during individual requests.

### Challenge 2: Real-time Inference
- **Problem:** Ensuring real-time inference without significant delays.
- **Solution:** Optimized the prediction function to handle inputs and provide predictions quickly, leveraging TensorFlow's efficient computation.

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- TensorFlow
- Uvicorn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/faisal-fida/codespaces-flask.git
   cd codespaces-flask
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Extract the TensorFlow model:
   ```bash
   python main.py
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

## Usage

1. Start the Flask app using the command above.
2. Access the API at `http://localhost:8000/`.
3. Use the `/predict/<symptoms>` endpoint to get disease predictions based on symptoms.
