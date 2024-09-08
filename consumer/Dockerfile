FROM python:3.9-slim

# Install necessary utilities like netcat-openbsd for network testing
RUN apt-get update && apt-get install -y iputils-ping netcat-openbsd

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY consumer.py .

CMD ["python", "consumer.py"]
