import random

opciones = ["piedra", "papel", "tijera"]

selecionUser= input("Selecione: Piedra,Papel,Tijera : ").lower()

selecionMaquina= random.choice(opciones)

print("Selecion usuario: ",selecionUser)

print("Selecion usuario: ",selecionMaquina)

if selecionUser not in opciones:
    print("Opcion invalida por el usuario")
    exit()
elif(selecionUser==selecionMaquina):
    print("Empate")
elif((selecionUser=="piedra" and selecionMaquina =="tijera")or
     (selecionUser=="tijera" and selecionMaquina =="papel")or
     (selecionUser=="papel" and selecionMaquina =="piedra")
     ):
    print("Gana Usuario")
else:
    print("Grana Maquina")



