FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y sysstat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /cpu
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "cpu.py"]