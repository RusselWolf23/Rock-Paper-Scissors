from Elementos import Elemento
class Tijeras(Elemento):
    def __init__(self):
        super().__init__("tijeras ✌️")

    def fight(self, elemento):

        match(elemento.nombre):
            case "piedra ✊":
                print("pierde")
                return 1

            case "papel 🖐️":
                print("GANA")
                return 2
                
            case "tijeras ✌️":
                print("empate")
                return 0

        return None
