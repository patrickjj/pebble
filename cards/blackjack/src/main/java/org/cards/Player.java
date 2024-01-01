package org.cards;

import java.util.ArrayList;
import java.util.HashMap;
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

        logger.log(Level.INFO, String.format("Card total: %d", cardTotal));
        return cardTotal < 17;
    }

    public boolean hit(HashMap<Integer, Integer> availableCards) {
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


        for (HashMap.Entry<Integer, Integer> entry : availableCards.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
        }
        logger.log(Level.INFO, String.format("Card total: %d", cardTotal));
        return cardTotal < 17;
    }
}
