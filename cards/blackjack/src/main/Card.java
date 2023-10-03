package main;

public class Card {

    private Suit suit;

    //Ace-King represented by 1-13
    private int rank;

    public enum Suit {
        Hearts,
        Spades,
        Clubs,
        Diamonds
    }



    public Card(int rank, Suit suit) {
        this.rank = rank;
        this.suit = suit;
    }

    @Override
    public String toString() {
        return "SUIT: " + suit + " RANK: " + rank;
    }
}
