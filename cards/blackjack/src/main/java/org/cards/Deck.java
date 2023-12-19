package org.cards;

public class Deck {

    private static final int NUM_CARDS = 52;
    //final array as it will never refer to anything else
    private final Card[] deck = new Card[NUM_CARDS];

    public Deck() {
        for (int i = 0; i < 13; i++){
            deck[i] = new Card(i+1, Card.Suit.Hearts);
            deck[i+13] = new Card(i+1, Card.Suit.Diamonds);
            deck[i+26] = new Card(i+1, Card.Suit.Clubs);
            deck[i+39] = new Card(i+1, Card.Suit.Spades);
        }
    }

    @Override
    public String toString() {
        StringBuilder output = new StringBuilder();
        for (Card card : deck) {
            output.append(card.toString()).append('\n');
        }
        return output.toString();
    }
}
