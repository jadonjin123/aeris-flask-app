# Import Python base image
FROM python:3.9-slim

# Establish the working directory
WORKDIR /aeris-flask-project

# Copy the file containing all packages
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files
COPY . .

# Open port that no other application is using
EXPOSE 5001

# Start Aeris Flask application
CMD ["python", "app.py", "--address=0.0.0.0"]
