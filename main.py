from Elementos import Elemento
from Piedra import Piedra
from Tijeras import Tijeras
from Papel import Papel
import time
import os
import random

# Códigos de escape ANSI para cambiar el color del texto


class Colores:
    RESET = '\033[0m'       # Restablecer el estilo
    NEGRO = '\033[30m'      # Texto en color negro
    ROJO = '\033[31m'       # Texto en color rojo
    VERDE = '\033[32m'      # Texto en color verde
    AMARILLO = '\033[33m'   # Texto en color amarillo
    AZUL = '\033[34m'       # Texto en color azul
    MAGENTA = '\033[35m'    # Texto en color magenta
    CYAN = '\033[36m'       # Texto en color cyan
    BLANCO = '\033[37m'     # Texto en color blanco


# Ejemplo de uso
print(Colores.ROJO + 'Este texto es de color rojo' + Colores.RESET)


piedra = Piedra()
papel = Papel()
tijera = Tijeras()

jugando = True

while jugando:

    while True:

        try:
            eleccionJugador = int(input("Piedra✊(1), Papel🖐️ (2) o Tijera✌️ (3)?\n [pulsa 4 para salir] "))

            if eleccionJugador > 4 or eleccionJugador < 1:
                raise ValueError("El número no es correcto")
            else:
                break

        except ValueError as err:
            print("El número no es correcto")

    if eleccionJugador==4:
        jugando = False
        break

    match(eleccionJugador):
        case 1:
            eleccionJugador = piedra
        case 2:
            eleccionJugador = papel
        case 3:
            eleccionJugador = tijera    
            
           
    eleccionCPU=random.randint(1,3)

    match(eleccionCPU):
        case 1:
            eleccionCPU = piedra
        case 2:
            eleccionCPU = papel
        case 3:
           eleccionCPU = tijera

    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")

    print(f"Tú:{eleccionJugador.nombre} CPU:{eleccionCPU.nombre}")
    eleccionJugador.fight(eleccionCPU)
    input("Presiona la tecla Enter para continuar")

    os.system("cls")
