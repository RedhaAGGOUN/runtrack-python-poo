# Remarque :
# Créez une classe Personne avec les attributs nom et prenom.
# Ajoutez une méthode SePresenter() qui affiche le nom complet de la personne.

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.prenom} {self.nom}."

# Instanciation de plusieurs objets et affichage
p1 = Personne("Dupont", "Jean")
p2 = Personne("Martin", "Alice")

print(p1.se_presenter())
print(p2.se_presenter())
