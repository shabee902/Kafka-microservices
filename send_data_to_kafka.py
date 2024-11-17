from kafka import KafkaProducer
import pandas as pd
import json
import time

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Load the CSV dataset
data_path = r'C:\Users\shabe\huge-ecommerce-dataset-1000000\huge_Ecommerce_dataset.csv'  # Update with the correct path
df = pd.read_csv(data_path)

# Iterate over each row and send data to Kafka
for index, row in df.iterrows():
    # Convert row to dictionary and then to JSON
    data = row.to_dict()
    producer.send('ecommerce_topic', value=data)
    
    # Optional: Sleep to simulate real-time streaming
    time.sleep(0.01)  # Adjust the sleep time as needed for your data flow rate

# Close the producer after sending all data
producer.flush()
producer.close()

print("Data has been sent to Kafka successfully.")
