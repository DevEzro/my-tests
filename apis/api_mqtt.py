from fastapi import FastAPI, HTTPException
from confluent_kafka import Producer, Consumer, KafkaError

app = FastAPI()

# Configuración del productor de Kafka
kafka_producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Cambia esto si tu servidor Kafka está en otra dirección
}
producer = Producer(kafka_producer_config)

# Configuración del consumidor de Kafka
kafka_consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mi-grupo',  # Nombre del grupo de consumidores
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(kafka_consumer_config)

# Endpoint para enviar mensajes a Kafka
@app.post("/enviar-mensaje/")
async def enviar_mensaje(mensaje: str):
    try:
        producer.produce('mi-tema', mensaje)
        producer.flush()  # Asegura que los mensajes se envíen
        return {"mensaje": "Mensaje enviado con éxito a Kafka"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el mensaje: {str(e)}")

# Endpoint para recibir mensajes de Kafka
@app.get("/recibir-mensajes/")
async def recibir_mensajes():
    consumer.subscribe(['mi-tema'])
    mensajes = []
    try:
        while True:
            msg = consumer.poll(1.0)  # Tiempo de espera en segundos
            if msg is None:
                break  # No hay más mensajes
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    break
                else:
                    raise KafkaError(msg.error())
            mensajes.append(msg.value().decode('utf-8'))
        return {"mensajes": mensajes}
    except KafkaError as e:
        raise HTTPException(status_code=500, detail=f"Error al recibir mensajes: {str(e)}")
    finally:
        consumer.close()