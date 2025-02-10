"""
Créer une classe Ville avec comme attributs privés un nom et un nombre d'habitants.
Créer une classe Personne avec les attributs privés suivants : nom, âge et un objet de la classe Ville.
Ajouter la méthode ajouterPopulation dans la classe Personne qui permet d’augmenter de 1 le nombre d’habitants de la ville.

Créer un objet Ville avec comme arguments “Paris” et 1000000.
Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
Créer les objets suivants :  
- John, 45 ans, habitant à Paris  
- Myrtille, 4 ans, habitant à Paris  
- Chloé, 18 ans, habitant à Marseille  

Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
"""

class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    def ajouter_habitant(self):
        self.__habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()

# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage des populations initiales
print(f"Population initiale de Paris : {paris.get_habitants()}")
print(f"Population initiale de Marseille : {marseille.get_habitants()}")

# Ajout des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage après l'ajout
print(f"Population de Paris après arrivée : {paris.get_habitants()}")
print(f"Population de Marseille après arrivée : {marseille.get_habitants()}")
