"""
Créer une classe Tache qui représente une tâche à faire.
Cette classe a comme attributs : un titre, une description et un statut (à faire ou terminé).

Créer une classe ListeDeTaches qui contient une liste de tâches avec les méthodes :
- ajouterTache : ajoute une tâche
- supprimerTache : supprime une tâche
- marquerCommeFinie : change le statut de la tâche
- afficherListe : affiche toutes les tâches
"""

class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "À faire"

    def marquerCommeFinie(self):
        self.__statut = "Terminée"

    def get_statut(self):
        return self.__statut

    def get_titre(self):
        return self.__titre

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        self.__taches.append(tache)

    def supprimerTache(self, titre):
        self.__taches = [t for t in self.__taches if t.get_titre() != titre]

    def afficherListe(self):
        for tache in self.__taches:
            print(f"{tache.get_titre()} - {tache.get_statut()}")

# Test
liste = ListeDeTaches()
t1 = Tache("Faire les courses", "Acheter du lait et du pain")
t2 = Tache("Réviser Python", "Passer en revue la POO")

liste.ajouterTache(t1)
liste.ajouterTache(t2)
t1.marquerCommeFinie()
liste.afficherListe()
