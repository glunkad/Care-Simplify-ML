# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN pip install --no-cache-dir vllm

# Expose the port the app runs on
EXPOSE 10000

# Run the model on container startup
CMD ["vllm", "serve", "m42-health/Llama3-Med42-8B", "--port 10000"]
