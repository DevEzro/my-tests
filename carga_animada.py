    print("[   ] Esperando a los elementos...", end='', flush=True)
    for i in range(12):  # 12 iteraciones para un total de 4 segundos (3 puntos, cambiando cada 0.33s)
        puntos = '.' * (i % 3 + 1)  # Genera 1, 2 o 3 puntos
        sys.stdout.write('\r[{}] Esperando a los elementos...'.format(puntos.ljust(3)))
        sys.stdout.flush()
        time.sleep(0.33)  # Cambia los puntos cada 0.33 segundos
    print("\n")
