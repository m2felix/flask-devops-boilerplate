# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first for caching benefits
COPY app/requirements.txt app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Copy the rest of the application code
COPY app/ app/

# Run tests during build (optional, you can remove this for speed)
# RUN pytest app/test_app.py

# Default command
CMD ["python", "app/main.py"]

