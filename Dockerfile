 FROM python:3.12-slim-bookworm

# Install system dependencies in one layer for efficiency
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy application files (assuming start.sh and app code are in repo root; adjust if in subdir)
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the start script (binds to $PORT automatically if your app/start.sh does)
CMD ["/app/start.sh"]
