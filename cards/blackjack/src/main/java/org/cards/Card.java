package org.cards;

public class Card {

    private final Suit suit;

    //Ace-King represented by 1-13
    private final int rank;

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

    public int value() {
        return Math.min(this.rank, 10);
    }

    public int getRank() {
        return rank;
    }
    @Override
    public String toString() {
        return "SUIT: " + suit + " RANK: " + rank;
    }
}
