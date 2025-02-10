class Student:
    """
    Créer une classe nommée Student qui a comme attributs privés un nom, un 
    prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro.
    """

    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, ID: {self.__numero_etudiant}, Niveau: {self.__level}")

# Test
etudiant = Student("Doe", "John", 145)
etudiant.add_credits(30)
etudiant.add_credits(40)
etudiant.add_credits(20)
etudiant.student_info()
