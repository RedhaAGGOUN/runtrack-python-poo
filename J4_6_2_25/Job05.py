/*
Job 5:
Récupérer votre classe Forme crée juste au-dessus.
Créer une classe fille nommée Cercle qui hérite de la classe Forme et possédant un attribut radius.
Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les différentes surcharges de la méthode aire en affichant les résultats en console.
*/

public class Main {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(5.0, 3.0);
        System.out.println("Aire du rectangle: " + rectangle.aire());
        
        Cercle cercle = new Cercle(4.0);
        System.out.println("Aire du cercle: " + cercle.aire());
    }
}

class Forme {
    public double aire() {
        return 0;
    }
}

class Rectangle extends Forme {
    private double largeur;
    private double hauteur;
    
    public Rectangle(double largeur, double hauteur) {
        this.largeur = largeur;
        this.hauteur = hauteur;
    }
    
    @Override
    public double aire() {
        return largeur * hauteur;
    }
}

class Cercle extends Forme {
    private double radius;
    
    public Cercle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public double aire() {
        return Math.PI * radius * radius;
    }
}
