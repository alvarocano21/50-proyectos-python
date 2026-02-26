

precioCuenta= float(input("Ingrese el total del la cuenta a dividir: "))
porcentajePropina= int(input(f"Ingresar % de la propina: "))
totalPersonas= int(input("Ingrese total personas a dividir: "))
print("")
totalCuenta = precioCuenta + ((precioCuenta * porcentajePropina) / 100)
precioPersona= totalCuenta/totalPersonas
print(f"Total de la cuenta: {precioCuenta}")
print("")
print(f"Total a pagar con {porcentajePropina}% de propina es de: {totalCuenta}  ")
print("")
print("Total a pagar por persona : ", round(precioPersona,2),"€")
print("")
