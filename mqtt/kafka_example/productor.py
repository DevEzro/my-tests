from confluent_kafka import Producer

# Configuración del productor
conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(conf)

# Función callback para reportar el estado de la entrega
def delivery_report(err, msg):
    if err is not None:
        print(f'Error en la entrega del mensaje: {err}')
    else:
        print(f'Mensaje entregado a {msg.topic()} [{msg.partition()}]')

# Enviar mensajes al tópico
for i in range(10):
    message = f'Mensaje número {i}'
    producer.produce('logs', message.encode('utf-8'), callback=delivery_report)

# Esperar a que se envíen todos los mensajes
producer.flush()
