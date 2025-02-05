# Créez une classe Produit avec les attributs nom, prixHT, et TVA.
# Ajoutez une méthode CalculerPrixTTC() qui retourne le prix TTC.
# Ajoutez une méthode afficher() pour afficher les informations du produit.

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculer_prix_TTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.calculer_prix_TTC()}"

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

# Instanciation et affichage des produits
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Téléphone", 500, 20)

print(produit1.afficher())
produit1.modifier_nom("PC Portable")
produit1.modifier_prix(1200)
print(produit1.afficher())

print(produit2.afficher())
