import pika

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar una cola llamada 'hello'
channel.queue_declare(queue='hello')

# Enviar un mensaje a la cola 'hello'
channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='¡Hola desde RabbitMQ!')

print(" [x] Mensaje enviado: ¡Hola desde RabbitMQ!")

# Cerrar la conexión
connection.close()