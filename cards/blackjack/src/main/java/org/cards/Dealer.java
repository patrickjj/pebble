package org.cards;

public class Dealer {

    private static final int NUM_DECKS = 1;
    //final array as it will never refer to anything else
    private final Deck deck[] = new Deck[NUM_DECKS];
}
