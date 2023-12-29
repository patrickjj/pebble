package org.cards;

import java.util.ArrayList;

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
}
