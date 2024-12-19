FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc git && apt-get clean

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run Gunicorn with Uvicorn worker
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:10000"]

