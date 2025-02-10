class Rectangle:
    """
    Créer une classe Rectangle avec des attributs privés, longueur et largeur 
    initialisées dans le constructeur.
    Créer des accesseurs et mutateurs afin de pouvoir afficher et modifier les 
    attributs de la classe.
    """

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'une instance de la classe Rectangle
rect = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Valeurs initiales:")
print(f"Longueur: {rect.get_longueur()}, Largeur: {rect.get_largeur()}")

# Modification des valeurs
rect.set_longueur(20)
rect.set_largeur(10)

# Vérification des modifications
print("Valeurs après modification:")
print(f"Longueur: {rect.get_longueur()}, Largeur: {rect.get_largeur()}")
