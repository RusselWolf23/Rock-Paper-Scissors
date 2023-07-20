from Elementos import Elemento
class Piedra(Elemento):
    def __init__(self):
        super().__init__("piedra ✊")

    def fight(self, elemento):

        match(elemento.nombre):
            case "piedra ✊":
                print("empate")
                return 0

            case "papel 🖐️":
                print("pierde")
                return 1

            case "tijeras ✌️":
                print("GANA")
                return 2

        return None
