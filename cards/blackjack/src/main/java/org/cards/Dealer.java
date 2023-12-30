package org.cards;

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.HashMap;

public class Dealer {

    private final Deck deck;
    public ArrayList<Card> cards;

    public Dealer(int numDecks) {
        deck = new Deck(numDecks);
        deck.shuffle();
        cards = new ArrayList<Card>(0);
    }

    public void dealCard(Player player) {
        player.cards.add(deck.yield());
    }

    public void dealCard() {
        this.cards.add(deck.yield());
    }

    public boolean hit() {
        int cardTotal = 0;
        int aces = 0;
        for(Card card : cards) {
            int val = card.value();
            if (val == 1) {
                aces += val;
            } else {
                cardTotal += val;
            }
        }
        if (aces > 0) {
            int remainder = 21 - cardTotal;
            int numHigh = remainder/11;
            aces -= numHigh;
            cardTotal += (aces + numHigh * 11);
        }

        return cardTotal < 17;
    }

    public HashMap<Integer, Integer> availableCardMap() {
        return deck.getAvailableCards();
    }
}
