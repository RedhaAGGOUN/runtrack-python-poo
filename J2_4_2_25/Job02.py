class Livre:
    """
    Créer la classe Livre qui prend en attributs privés un titre, un auteur et un 
    nombre de pages.
    Créer les accesseurs et mutateurs nécessaires afin de pouvoir modifier et 
    afficher les attributs.
    """

    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nombre_pages(nombre_pages)

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")

# Test
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(f"Titre: {livre.get_titre()}, Auteur: {livre.get_auteur()}, Pages: {livre.get_nombre_pages()}")

livre.set_nombre_pages(-10)  # Doit afficher une erreur
livre.set_nombre_pages(120)  # Modification correcte
print(f"Pages mises à jour: {livre.get_nombre_pages()}")
