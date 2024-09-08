FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY alert_consumer.py .

CMD ["python", "alert_consumer.py"]
