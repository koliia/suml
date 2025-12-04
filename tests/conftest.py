import sys
import os

# Get the path to the directory one level up (the project root)
# This directory contains 'predict.py'.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Insert the project root path at the beginning of the system path list.
# This ensures that imports like 'from predict import predict' are resolved
# by looking in the root directory first.
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Pytest automatically discovers and runs this file before collecting tests.
# No other code is needed here for path resolution.