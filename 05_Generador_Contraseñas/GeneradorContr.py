import random

#Esto para que coja numeros,letras,caracteres para la compraseña.
letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") #convertimos un string a lista 
numeros = list("0123456789") #convertimos un string a lista 
simbolos = list("!@#$%&*")#convertimos un string a lista 

cantidad_letras = int(input("¿Cuántas letras quieres? "))
cantidad_numeros = int(input("¿Cuántos números quieres? "))
cantidad_simbolos = int(input("¿Cuántos símbolos quieres? "))

password = []
# Aquí el "_" es perfecto porque no nos importa 
# si estamos en la vuelta 1 o en la 4, solo queremos sacar 5 letras.
for _ in range(cantidad_letras):#Necesito que este bucle se repita, pero no me interesa el valor del contador
    password.append(random.choice(letras))#append agrega elemento al final de la lista
    print(password)
for _ in range(cantidad_numeros):
    password.append(random.choice(numeros))   
    print(password)
for _ in range(cantidad_simbolos):
    password.append(random.choice(simbolos))
    print(password)
print(password)
print(f"Lista antes de mezclar: {password}")
print("Contraseña en string")
# Mezclar la lista shuffle no se asigna a variable)
random.shuffle(password)
print(password)
# .join une cada elemento de la lista con el separador que pongas entre las comillas ""
password_final = "".join(password)
print(password)
print(f"Tu contraseña final es: {password_final}")