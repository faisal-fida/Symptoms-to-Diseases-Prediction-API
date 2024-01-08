from flask import Flask, jsonify
from predict import predictions
import uvicorn

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the API"


@app.route("/predict/<string:symptoms>")
def predict(symptoms):
    predicted_disease, other_diseases = predictions(symptoms)
    return jsonify(
        {
            "predicted_disease": predicted_disease,
            "other_diseases": other_diseases,
        }
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
