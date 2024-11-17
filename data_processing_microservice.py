from confluent_kafka import Consumer, Producer
import pandas as pd
import json
import time

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'ecommerce_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)
consumer.subscribe(['ecommerce_topic'])

# Kafka producer configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Function to handle message delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

print("Starting to consume and process messages...")
try:
    data_buffer = []
    batch_size = 1000  # Adjust batch size as needed

    while True:
        msg = consumer.poll(1.0)  # Poll for a message
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        # Process the message
        record = json.loads(msg.value().decode('utf-8'))
        data_buffer.append(record)

        # Process in batches for efficiency
        if len(data_buffer) >= batch_size:
            df = pd.DataFrame(data_buffer)

            # Aggregation: Total number of transactions and average price per category
            if 'category' in df.columns:
                aggregated = df.groupby('category').agg(
                    transaction_count=('category', 'count'),
                    average_price=('price', 'mean')
                ).reset_index()

                # Send processed data to Kafka
                for _, row in aggregated.iterrows():
                    producer.produce('processed_ecommerce_topic', value=json.dumps(row.to_dict()), callback=delivery_report)
                    producer.poll(0)

                # Clear the buffer after processing
                data_buffer.clear()

            else:
                print("Column 'category' not found in the data. Skipping batch...")

        time.sleep(0.01)  # Optional, simulates processing delay

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    producer.flush()

print("Processing completed.")
