# Créez une classe Cercle avec un attribut rayon.
# Ajoutez des méthodes pour calculer la circonférence, l'aire et le diamètre.
# Créez deux cercles et affichez leurs informations.

import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficher_infos(self):
        print(f"Cercle de rayon {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Instanciation et affichage des cercles
c1 = Cercle(4)
c2 = Cercle(7)

for cercle in [c1, c2]:
    cercle.afficher_infos()
    print(f"Circonférence: {cercle.circonference()}")
    print(f"Aire: {cercle.aire()}")
    print(f"Diamètre: {cercle.diametre()}\n")
