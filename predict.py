# app/predict.py
from joblib import load
import numpy as np
import os

# Handle file paths gracefully (works in Jupyter too)
if "__file__" in globals():
    base_dir = os.path.dirname(__file__)
else:
    # Fallback when running interactively (e.g., Jupyter)
    base_dir = os.getcwd()

model_path = os.path.join(base_dir, "model.joblib")

# Load the trained model
model = load(model_path)

def predict(features):
    """
    Predict the Iris species based on input features.
    :param features: list or numpy array of 4 features [sepal_length, sepal_width, petal_length, petal_width]
    :return: Predicted class label (string)
    """
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]

    class_names = ['setosa', 'versicolor', 'virginica']
    return class_names[prediction]
