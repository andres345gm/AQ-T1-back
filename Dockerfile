# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from the correct directory to install dependencies
COPY ./app/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
