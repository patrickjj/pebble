package org.cards;

import java.util.HashMap;
import java.util.Random;

public class Deck {

    private static final int STANDARD_CARDS = 52;

    private static int NUM_CARDS;
    private int cardsDealt = 0;

    private int cardsRemaining;
    //final array as it will never refer to anything else
    private final Card[] cards;


    private final HashMap<Integer, Integer> availableCards;


    private final HashMap<Integer, Double> cardOdds;


    public Deck(int numDecks) {
        NUM_CARDS = STANDARD_CARDS * numDecks;
        cardsRemaining = NUM_CARDS;
        cards = new Card[NUM_CARDS];
        availableCards = new HashMap<>();
        cardOdds = new HashMap<>();

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
        for (HashMap.Entry<Integer, Integer> entry : availableCards.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            cardOdds.put(key, (value/(double) cardsRemaining));
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
        cardsRemaining--;
        int rank = returnCard.getRank();
        availableCards.put(rank, availableCards.get(rank) - 1);
        cardOdds.put(rank, (availableCards.get(rank)/(double) cardsRemaining));
        return returnCard;
    }

    public HashMap<Integer, Double> getCardOdds() {
        return cardOdds;
    }

}
