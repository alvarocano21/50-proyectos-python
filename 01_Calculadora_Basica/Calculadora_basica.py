
while True :
    
    selecion = str(input("Desea ingresar numeros o salir (si o no) ").lower())
    if selecion == 'si':
        numero1= int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))

        print("Operación deseda (+, -, *, /, salir)")
        selecion = str(input("Ingrese la operacion: "))

        if selecion =='+':
            print(numero1 + numero2)
        elif selecion =='-':
            print(numero1 - numero2)
        elif selecion == '*':
            print(numero1 * numero2)
        elif selecion == '/':
            print(numero1/numero2)
        elif selecion =='salir':
            print("Saliendo.............")
            break
        else:
            print("Opercion no Valida")
    elif selecion == 'no':
        print("Saliendo...........")
        break
    else:
        print("Opercion no Valida")
