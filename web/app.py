from flask import Flask
from flask import request
from flask import render_template

import base64
from PIL import Image
import io
import pandas as pd
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)
class_names = ['crosswalk', 'no parking', 'stop', 'turn left', 'turn right']
percentFilter = 0.95

# Model
model = tf.keras.models.load_model("savedModel")
def modelPredict(img):
    global model

    baseImage = base64.b64decode(img)
    pil_image = Image.open(io.BytesIO(baseImage)).resize((50, 50), Image.LANCZOS).convert("RGB") 
    img_array = np.asarray(pil_image)
    batch = np.expand_dims(img_array, axis=0)
    predictions = model.predict(batch)

    return predictions

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/predict", methods = ["POST"])
def predict():
    req = request.get_json(force = True)
    predictions = modelPredict(req["image"])[0]
    notRecognized = max(predictions) < percentFilter

    return {
        "predictions": predictions.tolist(),
        "prediction_classified": np.argmax(predictions).item(),
        "prediction_classified_class": "Not recognized" if notRecognized else class_names[np.argmax(predictions)],
        "class_names": class_names
    }

if __name__ == "__main__":
    app.run(debug=True)
