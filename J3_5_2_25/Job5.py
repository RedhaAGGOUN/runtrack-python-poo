"""
Créer un jeu de combat où un joueur et un ennemi s'affrontent.

Créer une classe Personnage avec :
- un nom
- un nombre de points de vie (vie)

Ajouter une méthode attaquer qui enlève des points de vie à l’adversaire.

Créer une classe Jeu qui :
- demande au joueur le niveau de difficulté (facile, moyen, difficile)
- initialise les personnages en fonction du niveau
- lance le combat en alternant les attaques

Ajouter une méthode vérifier_victoire pour afficher le gagnant une fois la partie terminée.
"""

import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)  # Dégâts aléatoires entre 5 et 15
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts !")
        if adversaire.vie < 0:
            adversaire.vie = 0
        print(f"{adversaire.nom} a maintenant {adversaire.vie} points de vie.\n")

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisir_niveau(self):
        while True:
            niveau = input("Choisissez un niveau de difficulté (facile/moyen/difficile) : ").lower()
            if niveau in ["facile", "moyen", "difficile"]:
                self.niveau = niveau
                break
            else:
                print("Niveau invalide. Veuillez choisir entre facile, moyen ou difficile.")

    def initialiser_personnages(self):
        if self.niveau == "facile":
            self.joueur = Personnage("Héros", 100)
            self.ennemi = Personnage("Gobelin", 50)
        elif self.niveau == "moyen":
            self.joueur = Personnage("Héros", 80)
            self.ennemi = Personnage("Orc", 80)
        else:
            self.joueur = Personnage("Héros", 60)
            self.ennemi = Personnage("Dragon", 120)

    def verifier_victoire(self):
        if self.joueur.vie <= 0:
            print("GAME OVER. L'ennemi a gagné !")
            return True
        elif self.ennemi.vie <= 0:
            print("Félicitations ! Vous avez vaincu l'ennemi !")
            return True
        return False

    def lancer_jeu(self):
        self.choisir_niveau()
        self.initialiser_personnages()
        print(f"\nCombat entre {self.joueur.nom} ({self.joueur.vie} PV) et {self.ennemi.nom} ({self.ennemi.vie} PV) !")

        # Combat en boucle jusqu'à ce que l'un des deux personnages ait 0 PV
        while not self.verifier_victoire():
            input("Appuyez sur Entrée pour attaquer...")
            self.joueur.attaquer(self.ennemi)
            if self.verifier_victoire():
                break
            self.ennemi.attaquer(self.joueur)

# Lancer le jeu
jeu = Jeu()
jeu.lancer_jeu()
