# Créez une classe Point avec les attributs x et y, initialisés dans le constructeur.
# Ajoutez des méthodes pour afficher et modifier les coordonnées.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_les_points(self):
        print(f"Coordonnées: ({self.x}, {self.y})")

    def changer_x(self, new_x):
        self.x = new_x

    def changer_y(self, new_y):
        self.y = new_y

# Instanciation et test des méthodes
point = Point(3, 7)
point.afficher_les_points()
point.changer_x(10)
point.changer_y(15)
point.afficher_les_points()