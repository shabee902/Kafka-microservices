Kafka Microservices Project

This repository contains the implementation of a real-time data processing pipeline using Apache Kafka, Docker, Python, and other modern technologies. The project demonstrates the processing, transformation, and aggregation of a large dataset in a distributed, scalable, and secure architecture.


Project Overview

The project aims to build a real-time backend for processing large-scale financial transaction data. It involves the following key functionalities:
- Data ingestion from a Kaggle dataset.
- Real-time preprocessing and transformation of the data.
- Aggregation and forwarding of the processed data for further use.
- Secure data transmission using SSL/TLS encryption.
- Containerization of microservices to ensure scalability, portability, and maintainability.


Features

- Data Ingestion: A producer service sends raw data from a Kaggle dataset (`huge-ecommerce-dataset`) to a Kafka topic.
- Real-Time Processing: A consumer service processes, transforms, and aggregates data using Tumbling and Sliding Window techniques.
- Secure Communication: Data is encrypted using SSL/TLS to ensure security during transmission.
- Scalable Architecture: Microservices are containerized using Docker and orchestrated using Docker Compose.
- Monitoring and Logging: Logs are monitored to ensure the reliability of the system.


Technologies Used


- Apache Kafka: Event-streaming platform for real-time data ingestion and processing.
- Docker & Docker Compose: For containerization and orchestration of services.
- Python: Core programming language for implementing microservices.
- Pandas: For data transformation and aggregation.
- OpenSSL: For generating SSL/TLS certificates.
- Kaggle Dataset: Financial transaction data for testing and simulation.


Architecture

1. Data Producer Microservice:
   - Reads data from a Kaggle dataset.
   - Sends data to the Kafka topic `ecommerce_topic`.

2. Data Consumer Microservice:
   - Consumes data from `ecommerce_topic`.
   - Processes and aggregates the data.
   - Publishes transformed data to `processed_ecommerce_topic`.

3. Kafka Broker:
   - Acts as the central hub for all data flow.
   - Manages topics and ensures reliability and scalability.

4. Secure Communication:
   - SSL/TLS encryption is enabled for Kafka to secure data transmission.
   - Access Control Lists (ACLs) are used for role-based access control.

5. Visualization:
   - Tools like Grafana are recommended for monitoring and reporting.

Setup Instructions

Prerequisites
1. Install Python 3.10 or later.
2. Install Docker and Docker Compose.
3. Clone the repository:  
   git clone https://github.com/shabee902/Kafka-microservices.git
   cd Kafka-microservices
   

Step 1: Set Up Kafka
1. Start the Kafka server in KRaft mode:
   bin/kafka-server-start.sh config/kraft/server.properties

2. Create the necessary topics:
   bin/kafka-topics.sh --create --topic ecommerce_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   bin/kafka-topics.sh --create --topic processed_ecommerce_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Step 2: Data Producer
1. Run the producer script to send data:
   python send_data_to_kafka.py

Step 3: Data Consumer
1. Run the consumer script to process data:
   python data_processing_microservice.py

Step 4: Containerization
1. Build and run Docker containers:
   docker-compose build
   docker-compose up -d

2. Verify running containers:
   docker ps

Step 5: Security Configuration
1. Generate SSL/TLS certificates using OpenSSL.
2. Update Kafka's `server.properties` to enable encryption and ACLs.

Step 6: Visualization
1. Use Grafana to create dashboards for monitoring processed data.


Project Breakdown

Phase 1: Konzeptionsphase
- Analyzed and selected technologies for the project.
- Designed a scalable architecture using Apache Kafka and microservices.

Phase 2: Implementierungsphase
- Implemented producer and consumer microservices.
- Added security layers for data protection.
- Containerized the system using Docker.

Phase 3: Finalisierungsphase
- Reviewed and optimized the system for reliability and scalability.
- Documented the entire workflow and submitted the final solution.


Future Improvements

1. Add batch processing pipelines for historical data.
2. Integrate advanced monitoring and alerting systems.
3. Enhance data governance capabilities with lineage tracking tools.

Repository Structure

- `send_data_to_kafka.py`: Producer microservice.
- `data_processing_microservice.py`: Consumer microservice.
- `docker-compose.yml`: Orchestration file for Docker.
- `Dockerfile`: Dockerfile for the microservices.
- `kafka.server.keystore.jks` & `kafka-cert`: SSL/TLS configuration files.


Contact

For any questions or suggestions, feel free to contact [Syed Shabee ul Hassan](mailto:abdemustufa786@gmail.com).
