import json
import psycopg2
import time
from kafka import KafkaConsumer

KAFKA_TOPIC = 'sensor_data'
KAFKA_SERVER = 'kafka:9092'
DB_HOST = 'postgres'
DB_NAME = 'sensor_data'
DB_USER = 'userkafka'
DB_PASS = 'password'

# Retry connecting to the database
print("hi")
print("Attempting to connect to database...")
while True:
    try:
        conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS)
        print("Database connection successful:", conn)
        break  # Exit loop if connection is successful
    except psycopg2.OperationalError as e:
        print(f"Database not ready, retrying in 5 seconds... Error: {e}")
        time.sleep(5)

cur = conn.cursor()

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, api_version=(0,11,5), value_deserializer=lambda v: json.loads(v.decode('utf-8')))

def save_to_db(data):
    cur.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)", (data['temperature'], data['humidity']))
    conn.commit()

if __name__ == '__main__':
    print("Main:")
    for message in consumer:
        sensor_data = message.value
        print(f"Consuming: {sensor_data}")
        save_to_db(sensor_data)
