# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Build the React app
WORKDIR /app/client
RUN npm install
RUN npm run build

# Set the working directory to the Flask app
WORKDIR /app/server

# Install Gunicorn
RUN pip install gunicorn

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
