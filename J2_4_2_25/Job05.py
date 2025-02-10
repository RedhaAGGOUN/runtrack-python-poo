class Voiture:
    """
    Créer une classe Voiture qui a pour attributs privés une marque, un modèle, 
    une année, un kilométrage et un attribut nommé en_marche initialisé par défaut à False.
    """

    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Carburant insuffisant pour démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir

# Test
voiture = Voiture("Toyota", "Corolla", 2022, 15000)
voiture.demarrer()
print("Voiture en marche:", voiture._Voiture__en_marche)
voiture.arreter()
print("Voiture en marche après arrêt:", voiture._Voiture__en_marche)
