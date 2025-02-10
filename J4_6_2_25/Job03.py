/*
Job 3:
Créer une classe Rectangle avec comme attribut privé longueur et largeur. Créer la méthode perimètre permettant de calculer le périmètre du rectangle ainsi que la méthode surface permettant de calculer la surface du rectangle.
Créer les assesseurs et mutateurs permettant de manipuler les attributs de la classe.
Créer une classe Parallelepipede héritant de la classe Rectangle avec en plus un attribut hauteur et une autre méthode volume, permettant de calculer le volume du parallélépipède.
Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.
*/

public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(5.0, 3.0);
        System.out.println("Périmètre: " + rect.perimetre());
        System.out.println("Surface: " + rect.surface());
        
        rect.setLongueur(6.0);
        rect.setLargeur(4.0);
        System.out.println("Nouveau périmètre: " + rect.perimetre());
        System.out.println("Nouvelle surface: " + rect.surface());
        
        Parallelepipede para = new Parallelepipede(6.0, 4.0, 10.0);
        System.out.println("Volume du parallélépipède: " + para.volume());
    }
}

class Rectangle {
    private double longueur;
    private double largeur;
    
    public Rectangle(double longueur, double largeur) {
        this.longueur = longueur;
        this.largeur = largeur;
    }
    
    public double perimetre() {
        return 2 * (longueur + largeur);
    }
    
    public double surface() {
        return longueur * largeur;
    }
    
    public double getLongueur() {
        return longueur;
    }
    
    public void setLongueur(double longueur) {
        this.longueur = longueur;
    }
    
    public double getLargeur() {
        return largeur;
    }
    
    public void setLargeur(double largeur) {
        this.largeur = largeur;
    }
}

class Parallelepipede extends Rectangle {
    private double hauteur;
    
    public Parallelepipede(double longueur, double largeur, double hauteur) {
        super(longueur, largeur);
        this.hauteur = hauteur;
    }
    
    public double volume() {
        return surface() * hauteur;
    }
    
    public double getHauteur() {
        return hauteur;
    }
    
    public void setHauteur(double hauteur) {
        this.hauteur = hauteur;
    }
}
