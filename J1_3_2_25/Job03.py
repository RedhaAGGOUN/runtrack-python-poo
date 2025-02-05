# Ajoutez une méthode addition() qui additionne "nombre1" et "nombre2", et affiche le résultat.

class Operation:
    def __init__(self, nombre1=5, nombre2=10):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

# Instanciation et affichage du résultat de l'addition
operation = Operation()
print(f"Addition result: {operation.addition()}")
