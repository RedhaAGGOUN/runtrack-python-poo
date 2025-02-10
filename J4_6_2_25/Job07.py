/*
Job 7:
Développer votre version du célèbre jeu Blackjack. Le but est de faire le plus de points sans dépasser 21. Chaque carte représente une valeur :
- de 2 à 10 : ces cartes ont pour valeur sa valeur nominale
- une figure a pour valeur 10 points
- un as 1 ou 11 points au choix

Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le joueur peut choisir de "prendre" (recevoir) une ou plusieurs cartes supplémentaires pour tenter d'améliorer sa main, ou de "passer" et laisser le tour au croupier. Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête. Si la main du joueur dépasse 21, il perd immédiatement. Si le total de la main du joueur est supérieur à celui du croupier, le joueur gagne. Sinon, c'est le croupier qui gagne.

Créer au minimum deux classes Carte et Jeu.
La classe Carte aura au minimum un attribut valeur et couleur. La classe Jeu quant à elle devra gérer l’ensemble des cartes. Les cartes du jeu seront stockées dans un attribut paquet représenté par une liste et contenant 52 cartes.
Créer toutes les méthodes nécessaires pour jouer une partie.
*/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

// Classe représentant une carte avec une valeur et une couleur
class Carte {
    private String valeur;
    private String couleur;
    
    public Carte(String valeur, String couleur) {
        this.valeur = valeur;
        this.couleur = couleur;
    }
    
    public String getValeur() {
        return valeur;
    }
    
    public String getCouleur() {
        return couleur;
    }
    
    @Override
    public String toString() {
        return valeur + " de " + couleur;
    }
}

// Classe gérant le jeu de cartes pour le Blackjack
class Jeu {
    private List<Carte> deck;
    
    public Jeu() {
        deck = new ArrayList<>();
        initializeDeck();
        shuffle();
    }
    
    // Initialise un paquet de 52 cartes
    private void initializeDeck() {
        String[] couleurs = {"Coeur", "Carreau", "Trèfle", "Pique"};
        String[] valeurs = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"};
        
        for (String couleur : couleurs) {
            for (String valeur : valeurs) {
                deck.add(new Carte(valeur, couleur));
            }
        }
    }
    
    // Mélange le paquet
    public void shuffle() {
        Collections.shuffle(deck);
    }
    
    // Pioche une carte dans le paquet
    public Carte drawCard() {
        if (deck.isEmpty()) {
            return null;
        }
        return deck.remove(0);
    }
    
    // Calcule la valeur totale d'une main en gérant l'as comme 11 ou 1
    public int calculateHandValue(List<Carte> hand) {
        int total = 0;
        int aces = 0;
        for (Carte carte : hand) {
            String val = carte.getValeur();
            if (val.equals("As")) {
                total += 11;
                aces++;
            } else if (val.equals("Valet") || val.equals("Dame") || val.equals("Roi")) {
                total += 10;
            } else {
                total += Integer.parseInt(val);
            }
        }
        // Ajustement pour les as si le total dépasse 21
        while (total > 21 && aces > 0) {
            total -= 10;
            aces--;
        }
        return total;
    }
}

// Classe principale pour lancer une partie de Blackjack
public class Main {
    public static void main(String[] args) {
        Jeu jeu = new Jeu();
        Scanner scanner = new Scanner(System.in);
        
        List<Carte> playerHand = new ArrayList<>();
        List<Carte> dealerHand = new ArrayList<>();
        
        // Distribuer 2 cartes au joueur et 2 cartes au croupier
        playerHand.add(jeu.drawCard());
        playerHand.add(jeu.drawCard());
        dealerHand.add(jeu.drawCard());
        dealerHand.add(jeu.drawCard());
        
        System.out.println("Vos cartes :");
        for (Carte carte : playerHand) {
            System.out.println(carte);
        }
        int playerTotal = jeu.calculateHandValue(playerHand);
        System.out.println("Total : " + playerTotal);
        
        // Tour du joueur
        boolean playerBust = false;
        while (true) {
            System.out.println("Voulez-vous prendre une carte (tapez 'hit') ou passer (tapez 'stand') ?");
            String decision = scanner.nextLine();
            if (decision.equalsIgnoreCase("hit")) {
                Carte drawn = jeu.drawCard();
                if (drawn == null) {
                    System.out.println("Plus de cartes dans le paquet.");
                    break;
                }
                playerHand.add(drawn);
                System.out.println("Vous avez reçu : " + drawn);
                playerTotal = jeu.calculateHandValue(playerHand);
                System.out.println("Total : " + playerTotal);
                if (playerTotal > 21) {
                    System.out.println("Vous avez dépassé 21. Vous perdez !");
                    playerBust = true;
                    break;
                }
            } else if (decision.equalsIgnoreCase("stand")) {
                break;
            } else {
                System.out.println("Commande non reconnue. Veuillez taper 'hit' ou 'stand'.");
            }
        }
        
        // Tour du croupier si le joueur n'a pas perdu
        if (!playerBust) {
            System.out.println("\nTour du croupier :");
            int dealerTotal = jeu.calculateHandValue(dealerHand);
            System.out.println("Cartes du croupier :");
            for (Carte carte : dealerHand) {
                System.out.println(carte);
            }
            System.out.println("Total du croupier : " + dealerTotal);
            
            while (dealerTotal < 17) {
                Carte drawn = jeu.drawCard();
                if (drawn == null) {
                    System.out.println("Plus de cartes dans le paquet.");
                    break;
                }
                dealerHand.add(drawn);
                System.out.println("Le croupier pioche : " + drawn);
                dealerTotal = jeu.calculateHandValue(dealerHand);
                System.out.println("Nouveau total du croupier : " + dealerTotal);
            }
            
            // Comparaison des totaux pour déterminer le gagnant
            if (dealerTotal > 21) {
                System.out.println("Le croupier a dépassé 21. Vous gagnez !");
            } else if (dealerTotal > playerTotal) {
                System.out.println("Le croupier gagne avec " + dealerTotal + " points contre " + playerTotal);
            } else if (dealerTotal < playerTotal) {
                System.out.println("Vous gagnez avec " + playerTotal + " points contre " + dealerTotal);
            } else {
                System.out.println("Match nul à " + playerTotal + " points.");
            }
        }
        
        scanner.close();
    }
}
