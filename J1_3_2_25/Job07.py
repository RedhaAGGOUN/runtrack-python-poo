# Créez une classe Personnage représentant un joueur sur un plateau (matrice).
# Ajoutez des méthodes gauche(), droite(), haut(), bas() pour déplacer le personnage.
# Ajoutez une méthode position() pour afficher ses coordonnées.

class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)

# Instanciation et test des déplacements
joueur = Personnage(0, 0)
joueur.droite()
joueur.haut()
print(f"Position actuelle: {joueur.position()}")
