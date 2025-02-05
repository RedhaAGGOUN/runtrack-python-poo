# Créez une classe Animal avec un attribut âge initialisé à 0.
# Ajoutez une méthode vieillir() pour incrémenter l'âge.
# Ajoutez une méthode nommer() pour attribuer un nom.

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation et test des méthodes
animal = Animal()
print(f"Âge
