import random

numeroMaquina = random.randint(1, 10)
intentos = 0

while True:
    try:
        numeroUser = int(input("Dime el número secreto (1-10): "))
    except ValueError:
        print("Debes ingresar un número.")
        continue

    # Validar rango
    if numeroUser < 1 or numeroUser > 10:
        print("Debes ingresar un número entre 1 y 10.")
        continue
    
    intentos += 1

    if numeroMaquina < numeroUser:
        print("El número secreto es MENOR")

    elif numeroMaquina > numeroUser:
        print("El número secreto es MAYOR")

    else:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")

        respuesta = input("¿Quieres continuar? (si/no): ").lower()

        if respuesta == "no":
            break
        else:
            numeroMaquina = random.randint(1, 10)
            intentos = 0
            print("Nuevo juego iniciado 🔄")