# Use a generic Python image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy requirement first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
