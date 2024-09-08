import json
import psycopg2
from kafka import KafkaConsumer

# Kafka configuration
KAFKA_TOPIC = 'sensor_data'
KAFKA_SERVER = 'kafka:9092'

# Thresholds for alerts
TEMP_THRESHOLD = 30.0  # Temperature above this will trigger an alert
HUMIDITY_THRESHOLD = 80.0  # Humidity above this will trigger an alert

# Create a Kafka consumer
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, api_version=(0,11,5), value_deserializer=lambda v: json.loads(v.decode('utf-8')))

def trigger_alert(sensor_data):
    temperature = sensor_data['temperature']
    humidity = sensor_data['humidity']
    
    alerts = []
    if temperature > TEMP_THRESHOLD:
        alerts.append(f"ALERT: High Temperature! Recorded: {temperature}°C (Threshold: {TEMP_THRESHOLD}°C)")
    
    if humidity > HUMIDITY_THRESHOLD:
        alerts.append(f"ALERT: High Humidity! Recorded: {humidity}% (Threshold: {HUMIDITY_THRESHOLD}%)")
    
    return alerts

if __name__ == '__main__':
    print("Alert Consumer is running and listening for sensor data...")
    
    # Consume messages from Kafka
    for message in consumer:
        sensor_data = message.value
        print(f"Received data: {sensor_data}")
        
        # Check for alerts
        alerts = trigger_alert(sensor_data)
        if alerts:
            for alert in alerts:
                print(alert)  # Log or print the alert
