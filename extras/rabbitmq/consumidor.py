import pika

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola 'hello' (esto asegura que exista)
channel.queue_declare(queue='hello')

# Definir una función de callback que maneje los mensajes
def callback(ch, method, properties, body):
    print(f" [x] Recibido {body}")

# Configurar el consumidor para escuchar la cola 'hello'
channel.basic_consume(queue='hello',
                    on_message_callback=callback,
                    auto_ack=True)

print(' [*] Esperando mensajes. Para salir presiona CTRL+C')

# Iniciar el consumo
channel.start_consuming()
