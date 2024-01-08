import tensorflow as tf
from tensorflow import keras
import json
import uvicorn

# Load the keras model from model.keras
model = tf.keras.models.load_model("model/tf_model")

# Load classes from the file
with open("model/classes.json", "r") as f:
    classes = json.load(f)


def predictions(text: str) -> str:
    """
    Predicts the disease based on the symptoms
    :param text: The symptoms
    :return: The predicted disease
    """
    feature = {"text": text}
    input_dict = {
        name: tf.convert_to_tensor([value]) for name, value in feature.items()
    }
    predictions = model.predict(input_dict, verbose=0)[0]
    predicted_disease = classes[tf.argmax(predictions).numpy()]
    other_diseases = [
        (classes[i], predictions[i])
        for i in range(len(predictions))
        if i != tf.argmax(predictions).numpy()
    ]
    return predicted_disease, other_diseases
