
# Crear diccionario FUERA del bucle
operaciones = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b
}
while True :
    
    confirmacion = input("Desea ingresar numeros o salir (si o no) :").lower()
    if confirmacion == 'si':
        numero1= int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))
        print("Operación deseda (+, -, *, /, salir)")
        selecion = input("Ingrese la operacion: ").lower()
        if selecion in operaciones:
            print(f"Resultado de la {selecion} de {numero1} {selecion} {numero2} es:" , operaciones[selecion](numero1,numero2))
        elif selecion == 'salir':
            print("Saliendo........")
            break
        else:
            print("Opercion no Valida")
    elif confirmacion == 'no':
        print("Saliendo........")
        break
    else:
        print("Opercion no Valida........")
