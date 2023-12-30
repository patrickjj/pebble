package org.cards;

import java.util.HashMap;
import java.util.Random;

public class Deck {

    private static final int STANDARD_CARDS = 52;

    private static int NUM_CARDS;
    private int cardsDealt = 0;
    //final array as it will never refer to anything else
    private final Card[] cards;


    private HashMap<Integer, Integer> availableCards;


    public Deck(int numDecks) {
        NUM_CARDS = STANDARD_CARDS * numDecks;
        cards = new Card[NUM_CARDS];
        availableCards = new HashMap<>();
        int count = 0;
        for (int j = 0; j < numDecks; j ++) {
            for (int i = 0; i < 13; i++){
                cards[i + j * STANDARD_CARDS] = new Card(i+1, Card.Suit.Hearts);
                cards[i+13 + j * STANDARD_CARDS] = new Card(i+1, Card.Suit.Diamonds);
                cards[i+26 + j * STANDARD_CARDS] = new Card(i+1, Card.Suit.Clubs);
                cards[i+39 + j * STANDARD_CARDS] = new Card(i+1, Card.Suit.Spades);
                count = availableCards.getOrDefault(i+1, 0);
                availableCards.put(i+1, count + 4);
            }
        }

    }

    public void shuffle() {

        //fisher yates
        for (int i = NUM_CARDS-1; i > 0; i--) {

            int j = (int) Math.floor(i * Math.random());

            Card temp = cards[i];
            cards[i] = cards[j];
            cards[j] = temp;
        }
    }

    @Override
    public String toString() {
        StringBuilder output = new StringBuilder();
        for (Card card : cards) {
            output.append(card.toString()).append('\n');
        }
        return output.toString();
    }

    public Card yield() {
        Card returnCard = cards[cardsDealt++];
        int rank = returnCard.getRank();
        availableCards.put(rank, availableCards.get(rank) - 1);
        return returnCard;
    }

    public HashMap<Integer, Integer> getAvailableCards() {
        return availableCards;
    }
}
