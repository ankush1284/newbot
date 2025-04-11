FROM python:3.10-slim

WORKDIR /app

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip first
RUN pip install --upgrade pip

# 3. Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application
COPY . .

# 5. Run the bot
CMD ["python", "main.py"]
