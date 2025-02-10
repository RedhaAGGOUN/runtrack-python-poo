/*
Créer une classe Vehicule avec comme attribut une marque, le modèle, une année et un prix. 
Créer la méthode informationsVehicule qui écrit en console la marque, le modèle, l'année et le prix du véhicule.
Créer la classe Voiture qui hérite de la classe Vehicule. Dans le constructeur de la classe Voiture, ajouter un attribut portes qui contient le nombre entier 4. 
Créer dans cette classe, une méthode informationsVehicule qui affiche, en console, les informations générales du véhicule et le nombre de portes de la voiture.
Créer une classe Moto qui hérite de la classe Vehicule et ajouter l'attribut roue qui contient par défaut l’entier 2. 
Créer à nouveau une méthode informationsVehicule dans la classe Moto qui affiche l'intégralité des informations de la moto.
Instancier un objet Moto et faites appel à la méthode informationsVehicule.
Créer la méthode demarrer dans la classe Vehicule qui écrit en console “Attention, je roule”. 
Surcharger la méthode demarrer dans la classe Moto et Voiture afin d’afficher un message personnalisé.
Faites démarrer votre voiture et votre moto.
*/

public class Main {
    public static void main(String[] args) {
        // Instanciation d'un objet Voiture et affichage de ses informations
        Voiture voiture = new Voiture("Toyota", "Corolla", 2020, 20000.0);
        voiture.informationsVehicule();
        voiture.demarrer();
        
        // Instanciation d'un objet Moto et affichage de ses informations
        Moto moto = new Moto("Yamaha", "MT-07", 2021, 7500.0);
        moto.informationsVehicule();
        moto.demarrer();
    }
}

class Vehicule {
    private String marque;
    private String modele;
    private int annee;
    private double prix;
    
    public Vehicule(String marque, String modele, int annee, double prix) {
        this.marque = marque;
        this.modele = modele;
        this.annee = annee;
        this.prix = prix;
    }
    
    public void informationsVehicule() {
        System.out.println("Marque: " + marque + ", Modèle: " + modele + ", Année: " + annee + ", Prix: " + prix);
    }
    
    public void demarrer() {
        System.out.println("Attention, je roule");
    }
}

class Voiture extends Vehicule {
    private int portes;
    
    public Voiture(String marque, String modele, int annee, double prix) {
        super(marque, modele, annee, prix);
        this.portes = 4;
    }
    
    @Override
    public void informationsVehicule() {
        super.informationsVehicule();
        System.out.println("Nombre de portes: " + portes);
    }
    
    @Override
    public void demarrer() {
        System.out.println("La voiture démarre en douceur.");
    }
}

class Moto extends Vehicule {
    private int roue = 2;
    
    public Moto(String marque, String modele, int annee, double prix) {
        super(marque, modele, annee, prix);
    }
    
    @Override
    public void informationsVehicule() {
        super.informationsVehicule();
        System.out.println("Nombre de roues: " + roue);
    }
    
    @Override
    public void demarrer() {
        System.out.println("La moto démarre avec un rugissement.");
    }
}
