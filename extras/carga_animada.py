import sys

    print("[   ] Esperando a los elementos...", end='', flush=True) # Muestra el mensaje, sin añadir una linea nueva e inmediatamente
    for i in range(12):  # Bucle de 12 iteracciones
        puntos = '.' * (i % 4)  # Muestra los puntos animados de ninguno a los 3
        sys.stdout.write('\r[{}] Esperando a los elementos...'.format(puntos.ljust(3))) # Indica el ancho de caracteres
        sys.stdout.flush() # Indica que lo muestre de inmediato
        time.sleep(0.33)  # Pausa al final de cada iteraccion durante o.33
