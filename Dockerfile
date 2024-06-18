# Use a lightweight base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR
RUN apt update && apt install tesseract-ocr -y

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add the project files to the container
Add runserver.py .
Add server server
Add db db
Add api api

# Expose the port on which the FastAPI server will run
EXPOSE 2121

# Start the FastAPI server
CMD ["python", "runserver.py"]