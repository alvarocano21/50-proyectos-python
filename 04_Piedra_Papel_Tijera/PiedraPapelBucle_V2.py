import random

opciones = ["piedra", "papel", "tijera"]
puntoUser = 0
puntoMaquina = 0
while True:
    selecionUser= input("Selecione: Piedra,Papel,Tijera,Salir: ").lower()

    selecionMaquina= random.choice(opciones)

    if selecionUser == "salir":
        print("\nMarcador final:")
        print("--------------------")
        print("---Usuario:", puntoUser)
        print("---Máquina:", puntoMaquina)
        print("--------------------")
        print("")
        break

    if selecionUser not in opciones:
        print("\nOpcion invalida por el usuario")
        continue

    selecionMaquina= random.choice(opciones)
    print("---Usuario:", selecionUser)
    print("---Máquina:", selecionMaquina)

    if(selecionUser==selecionMaquina):
        print("Empate")
    elif((selecionUser=="piedra" and selecionMaquina =="tijera")or
        (selecionUser=="tijera" and selecionMaquina =="papel")or
        (selecionUser=="papel" and selecionMaquina =="piedra")
        ):
        print("Gana Usuario")
        puntoUser+=1
    else:
        print("Grana Maquina")
        puntoMaquina+=1
    print("--------------------")
    print(f"--------------------USUARIO: ",puntoUser," --------------------MAQUINA: ",puntoMaquina)
    print("--------------------")
    print("")


