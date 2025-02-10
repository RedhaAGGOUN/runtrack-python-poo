"""
Créer une classe Joueur qui représente un joueur de football.
Cette classe doit avoir les attributs suivants : 
- nom
- numéro
- position
- nombre de buts marqués
- passes décisives effectuées
- cartons jaunes reçus
- cartons rouges reçus

Les méthodes suivantes doivent être présentes :
- marquerUnBut : augmente le nombre de buts
- effectuerUnePasseDecisive : augmente le nombre de passes décisives
- recevoirUnCartonJaune : ajoute un carton jaune
- recevoirUnCartonRouge : ajoute un carton rouge
- afficherStatistiques : affiche les stats du joueur

Créer une classe Equipe qui représente une équipe de football.
Elle doit avoir les attributs :
- nom
- liste des joueurs

Les méthodes suivantes doivent être présentes :
- ajouterJoueur : ajoute un joueur à l’équipe
- afficherStatistiquesJoueurs : affiche les stats de tous les joueurs
- mettreAJourStatistiquesJoueur : met à jour les stats d’un joueur

Simuler un match : marquer un but, donner un carton, et afficher les statistiques mises à jour.
"""

class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0

    def marquerUnBut(self):
        self.__buts += 1

    def effectuerUnePasseDecisive(self):
        self.__passes += 1

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.__nom} (#{self.__numero}, {self.__position}) - Buts: {self.__buts}, Passes: {self.__passes}, Cartons Jaunes: {self.__cartons_jaunes}, Cartons Rouges: {self.__cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.__nom}:")
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

# Simulation d'un match
equipe = Equipe("Marseille")
joueur1 = Joueur("Payet", 10, "Milieu")
joueur2 = Joueur("Benedetto", 9, "Attaquant")

equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)

# Actions du match
joueur1.marquerUnBut()
joueur2.recevoirUnCartonJaune()

# Affichage des statistiques après le match
equipe.afficherStatistiquesJoueurs()
