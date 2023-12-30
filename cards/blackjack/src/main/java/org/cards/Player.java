package org.cards;

import java.util.ArrayList;
import java.util.logging.*;

public class Player {
    public ArrayList<Card> cards;
    public final int id;
    private Logger logger;
    public Player(Logger logger, int id) {
        this.id = id;
        this.logger = logger;
        cards = new ArrayList<Card>(0);
    }

    public boolean hit() {
        int cardTotal = 0;
        for(Card card : cards) {
            cardTotal += card.value();
        }

        logger.log(Level.INFO, String.format("Card total: %d", cardTotal));
        return cardTotal < 17;
    }
}
