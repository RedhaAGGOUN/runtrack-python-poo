# Modifiez la classe Operation et affichez en console les valeurs des attributs "nombre1" et "nombre2".

class Operation:
    def __init__(self):
        self.nombre1 = 5
        self.nombre2 = 10

# Instanciation et affichage des attributs
operation = Operation()
print(f"Nombre1: {operation.nombre1}")
print(f"Nombre2: {operation.nombre2}")
