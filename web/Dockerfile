# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
