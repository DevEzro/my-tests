#!/usr/bin/env python
import pika
# Inicializa la conexión (bloqueante: hasta que no se completa se queda detenida)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# Inicializa el canal de comunicación
channel = connection.channel()
# Declara una cola llamada 'hello'
channel.queue_declare(queue='hello')
# Envío del mensaje 'Hola mundo!' a través de la cola de destino 'hello'
channel.basic_publish(exchange='', routing_key='hello', body='Hola mundo!')
# Mensaje a enviar impreso por pantalla
print(" [->] Hola mundo!")
# Cierra la conexión
connection.close()