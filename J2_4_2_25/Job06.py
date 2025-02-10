class Commande:
    """
    Créer une classe Commande avec les attributs privés, numéro de 
    commande, liste de plats commandés et statut de la commande.
    """

    def __init__(self, numero):
        self.__numero = numero
        self.__plats = {}
        self.__statut = "En cours"

    def ajouter_plat(self, nom, prix):
        self.__plats[nom] = prix

    def annuler(self):
        self.__statut = "Annulée"
        self.__plats = {}

    def calculer_total(self):
        return sum(self.__plats.values())

    def afficher_commande(self):
        print(f"Commande {self.__numero} - Statut: {self.__statut}")
        for plat, prix in self.__plats.items():
            print(f"{plat}: {prix}€")
        print(f"Total: {self.calculer_total()}€")

# Test
commande = Commande(12345)
commande.ajouter_plat("Pizza", 12)
commande.ajouter_plat("Pasta", 10)
commande.afficher_commande()
commande.annuler()
commande.afficher_commande()
