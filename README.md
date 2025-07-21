# Assignment_Day26_Streaming_Pipeline
This repo is for Assignment Day 26 - Streaming for Data Pipeline
This project demonstrates a simple real-time ETL pipeline using Apache Kafka and PySpark Streaming.
maaf sebelumnya mas thosan, saya telat dan masih banyak kekurangannya ya :(

Requirements
- Docker & Docker Compose
- Python around 3.8+
- PySpark
- kafka-python

 Step Instructions
1. Start Kafka and Zookeeper : docker-compose up -d
2. Install Python Requirements (Recommended in a virtual environment): pip install -r requirements.txt
3. Start Kafka Producer: python producer/producer.py
This will continuously send JSON-formatted purchasing events every 5 seconds.
4. Run Spark Streaming Job: spark-submit spark/spark_streaming.py
This will consume events from Kafka and print the daily running total of purchases to the console.
