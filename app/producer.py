from aiokafka import AIOKafkaProducer
import asyncio
import json
import logging

kafka_bootstrap_servers = 'kafka-service.kafka.svc.cluster.local:9092'

async def send_message(topic: str, message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
    await producer.start()
    try:
        value = json.dumps(message).encode("utf-8")
        await producer.send_and_wait(topic, value)
        logging.info(f"Message sent to topic '{topic}': {message}")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
    finally:
        await producer.stop()