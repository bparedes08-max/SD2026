import time

def ciclo():
    cnt = 0
    print("iniciando ciclo...")
    while True:
        try:
            time.sleep(1)
            print(f"{cnt}: Ejecutando...")
            cnt += 1
            new_func()
        except KeyboardInterrupt:
            print("Ciclo interrumpido por el usuario.")
            break

def new_func():
    time.sleep(1)

if __name__ == "__main__":
    ciclo()