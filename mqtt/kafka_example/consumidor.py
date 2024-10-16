from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuración del consumidor
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "mi-grupo",
    'auto.offset.reset': 'earliest'
}

# Inicializa el consumidor y suscribe al tópico 'logs'
consumer = Consumer(conf)
consumer.subscribe(['logs'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f"Mensaje recibido: {msg.value().decode('utf-8')}")
finally:
    consumer.close()
