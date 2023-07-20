from Elementos import Elemento
class Papel(Elemento):
    def __init__(self):
        super().__init__("papel 🖐️")

    def fight(self, elemento):

        match(elemento.nombre):
            case "piedra ✊":
                print("GANA")
                return 2

            case "papel 🖐️":
                print("empate")
                return 0
                
            case "tijeras ✌️":
                print("pierde")
                return 1

        return None
