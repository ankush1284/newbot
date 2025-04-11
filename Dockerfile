# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Set environment variables (or pass during docker run)
ENV API_ID=your_id
ENV API_HASH=your_hash
ENV BOT_TOKEN=your_token
ENV DATABASE_URI=your_mongodb_uri

# Start command
CMD ["python", "main.py"]
