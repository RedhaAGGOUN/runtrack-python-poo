/*
Job 2:
À l’aide de la classe Personne, Eleve et Professeur créés au-dessus, faites dire bonjour à votre élève grâce à la méthode bonjour ainsi que “Je vais en cours” grâce à la méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.
Créez un objet Professeur, 40 ans, faites dire bonjour à votre professeur et commencez le cours grâce à la méthode enseigner.
*/

class Personne {
    protected int age = 14;
    
    public void afficherAge() {
        System.out.println(age);
    }
    
    public void bonjour() {
        System.out.println("Hello");
    }
    
    public void modifierAge(int nouveauAge) {
        age = nouveauAge;
    }
}

class Eleve extends Personne {
    public void allerEnCours() {
        System.out.println("Je vais en cours");
    }
    
    @Override
    public void afficherAge() {
        System.out.println("J'ai " + age + " ans");
    }
}

class Professeur extends Personne {
    private String matiereEnseignee;
    
    public Professeur(String matiere, int age) {
        this.matiereEnseignee = matiere;
        this.age = age;
    }
    
    public void enseigner() {
        System.out.println("Le cours va commencer");
    }
}

public class Main {
    public static void main(String[] args) {
        Eleve eleve = new Eleve();
        eleve.bonjour();
        eleve.allerEnCours();
        eleve.modifierAge(15);
        
        Professeur professeur = new Professeur("Mathématiques", 40);
        professeur.bonjour();
        professeur.enseigner();
    }
}
