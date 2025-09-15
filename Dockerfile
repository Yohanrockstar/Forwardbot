FROM python:3.12-slim-bookworm

RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y git gcc python3-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
    
WORKDIR /app
COPY main.py /app/main.py
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
