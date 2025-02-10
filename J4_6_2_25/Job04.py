/*
Job 4:
Créer une classe nommée Forme possédant une méthode nommée aire qui renvoie 0.
Créer une classe Rectangle qui hérite de la classe Forme et qui possède deux attributs largeur et hauteur.
Surcharger la méthode aire dans la classe Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
Écrire en console le résultat de la méthode aire de la classe Rectangle.
*/

public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(5.0, 3.0);
        System.out.println("L'aire du rectangle est: " + rect.aire());
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
