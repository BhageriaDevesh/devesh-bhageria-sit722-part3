# Updated Dockerfile for book_catalog and inventory_management

# Use a stable Python base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the necessary dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Command to run the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
