class Livre:
    """
    Ajouter l'attribut privé suivant :  
    - disponible est initialisé par défaut à True.
    """

    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nombre_pages(nombre_pages)
        self.__disponible = True

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Le livre est déjà emprunté.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Le livre est déjà disponible.")

# Test
livre = Livre("1984", "George Orwell", 328)
print("Disponible:", livre.verification())
livre.emprunter()
print("Disponible après emprunt:", livre.verification())
livre.rendre()
print("Disponible après retour:", livre.verification())
