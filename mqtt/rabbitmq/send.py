import pika
from colorama import Fore
print(r"""
 _____ _____ _   _______
/  ___|  ___| \ | |  _  \
\ `--.| |__ |  \| | | | |
 `--. \  __|| . ` | | | |
/\__/ / |___| |\  | |/ /
\____/\____/\_| \_/___/  
""")
# Inicializa la conexión (bloqueante: hasta que no se completa se queda detenida)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# Inicializa el canal de comunicación
channel = connection.channel()

# Declara una cola llamada 'hello'
channel.queue_declare(queue='hello')
body = input(f"{Fore.CYAN}[-]{Fore.RESET} Introduce un mensaje para el destinatario: ")

# Envío del mensaje 'Hola mundo!' a través de la cola de destino 'hello'
channel.basic_publish(exchange='', routing_key='hello', body=body)

# Mensaje a enviar impreso por pantalla
print(f"{Fore.YELLOW}[->]{Fore.RESET} Enviando mensaje '{body}'")

# Cierra la conexión
connection.close()