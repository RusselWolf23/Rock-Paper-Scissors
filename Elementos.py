class Elemento:
    def __init__(self, nombre):
        self.nombre=nombre
        
    def fight(self, elemento):
        return 0

# class Piedra(Elemento):
#     def __init__(self):
#         super().__init__("piedra")

#     def fight(self, elemento):

#         match(elemento.nombre):
#             case "piedra":
#                 print("empate")
#                 return 0

#             case "papel":
#                 print("pierde")
#                 return 1

#             case "tijera":
#                 print("GANA")
#                 return 2

#         return 0
