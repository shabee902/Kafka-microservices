from kafka import KafkaConsumer
import json

# Kafka consumer configuration
consumer = KafkaConsumer(
    'ecommerce_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic
    enable_auto_commit=True,
    group_id='ecommerce_consumer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Starting to consume messages...")
for message in consumer:
    print(f"Received: {message.value}")
