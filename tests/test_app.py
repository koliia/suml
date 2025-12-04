# tests/test_app.py
import pytest
import os
import sys

# Add the application directory to the path so we can import predict
# This is necessary because the test is run from the root, but the module is one level up
# in the 'app' directory, or in this case, next to the 'tests' directory.
# Assuming predict.py is in the root directory for simplicity in CI,
# but if it was in 'app/predict.py', the import would need adjustment.
# Based on your previous files, predict.py seems to be in the root directory.

# If 'predict.py' is in the root:
from predict import predict

# If 'predict.py' is in a folder named 'app' (as suggested by the file contents):
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# from app.predict import predict

# Standard Iris example features (versicolor)
VERSICOLOR_FEATURES = [6.0, 2.9, 4.5, 1.5]


def test_prediction_output_is_string():
    """
    Test that the predict function returns a string (the class name).
    """
    prediction = predict(VERSICOLOR_FEATURES)

    # Assert that the output is a string class name
    assert isinstance(prediction, str)

    # Assert that the output is one of the valid class names
    valid_classes = ['setosa', 'versicolor', 'virginica']
    assert prediction in valid_classes