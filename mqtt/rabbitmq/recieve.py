import pika, sys, os
from colorama import Fore

def main():
    print(r"""
______ _____ _____ _____ _____ _   _ _____ 
| ___ \  ___/  __ \_   _|  ___| | | |  ___|
| |_/ / |__ | /  \/ | | | |__ | | | | |__  
|    /|  __|| |     | | |  __|| | | |  __| 
| |\ \| |___| \__/\_| |_| |___\ \_/ / |___ 
\_| \_\____/ \____/\___/\____/ \___/\____/ 
""")
    # Inicializa la conexión (bloqueante: hasta que no se completa se queda detenida)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    
    # Inicializa el canal de comunicación
    channel = connection.channel()
    
    # Declara una cola llamada 'hello'
    channel.queue_declare(queue='hello')
    
    # Método al que se llama cada vez que reciba un mensaje acaompañado de un mensaje
    # por pantalla
    def callback(ch, method, properties, body):
        message = body.decode('utf-8') # Convierte el body de byte string a UTF-8
        print(f"{Fore.GREEN}[+]{Fore.RESET} Mensaje recibido: '{message}' ")
    
    # Config. del consumidor para que escuche la cola, use la función anterior y 
    # confirme la recepción del mensaje
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    
    # Ciclo de espera del mensaje junto a un mensaje por pantalla
    print(f"{Fore.CYAN}[-]{Fore.RESET} Esperando a los mensajes...")
    channel.start_consuming()

# Manejo de la ejecucción y cierre limpios
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)