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

class Professeur {
    private String matiereEnseignee;

    public Professeur(String matiere) {
        this.matiereEnseignee = matiere;
    }

    public void enseigner() {
        System.out.println("Le cours va commencer");
    }
}

public class Main {
    public static void main(String[] args) {
        Personne personne = new Personne();
        Eleve eleve = new Eleve();
        eleve.afficherAge();
    }
}
