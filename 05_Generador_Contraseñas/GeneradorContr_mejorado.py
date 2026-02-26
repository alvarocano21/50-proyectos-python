import random

# 1. Preparación de datos
letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") 
numeros = list("0123456789") 
simbolos = list("!@#$%&*")

while True:

    #Entradas del usuario
    try:
        cantidad_letras = int(input("¿Cuántas letras quieres? "))
        cantidad_numeros = int(input("¿Cuántos números quieres? "))
        cantidad_simbolos = int(input("¿Cuántos símbolos quieres? "))
    except ValueError:
        print("Error: Debes ingresar solo números.")
    exit()

    # Validación de los 8 caracteres
    total_caracteres = cantidad_letras + cantidad_numeros + cantidad_simbolos

    if total_caracteres < 8:
        print(f"Atención: Tu contraseña solo tiene {total_caracteres} caracteres.")
        print("Se recomienda un mínimo de 8 para que sea segura.")
        exit()
    else:
        print(f"Genial, tu contraseña tendrá {total_caracteres} caracteres.")

    #Construcción de la lista
    password = []

    for _ in range(cantidad_letras):
        password.append(random.choice(letras))

    for _ in range(cantidad_numeros):
        password.append(random.choice(numeros))   

    for _ in range(cantidad_simbolos):
        password.append(random.choice(simbolos))

    # Mezcla y conversión
    random.shuffle(password)
    password_final = "".join(password)

    print("------------------------------")
    print(f"Tu contraseña final es: {password_final}")