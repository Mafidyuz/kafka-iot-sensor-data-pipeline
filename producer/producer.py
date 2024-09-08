import random
import time
import json
from kafka import KafkaProducer

KAFKA_TOPIC = 'sensor_data'
KAFKA_SERVER = 'kafka:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, api_version=(0,11,5), value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_sensor_data():
    temperature = round(random.uniform(10.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    return {
        'temperature': temperature,
        'humidity': humidity
    }

if __name__ == '__main__':
    while True:
        sensor_data = generate_sensor_data()
        print(f"Producing: {sensor_data}")
        producer.send(KAFKA_TOPIC, sensor_data)
        time.sleep(2)  # Send data every 2 seconds
