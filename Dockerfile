# Dockerfile

# Stage 1: Use an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
# This is a good practice to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
# We assume the model.joblib file is in the same directory as the Dockerfile
COPY . /app

# Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit application
# The Streamlit command is: streamlit run <your_app_file.py>
CMD ["streamlit", "run", "app.py"]