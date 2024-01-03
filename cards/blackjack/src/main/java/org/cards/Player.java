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

    public boolean hit(HashMap<Integer, Double> cardOdds) {
        //softTotal is used for when an ace is counted as an 11
        //hardTotal is for only low ace. The naming is a bit off technically as, classically, the hard hand is when your ace(s) must be low. In this case, it is not necessarily true.
        int softTotal = 0;
        int hardTotal = 0;
        int aces = 0;
        for(Card card : cards) {
            int val = card.value();
            if (val == 1) {
                aces += val;
            } else {
                softTotal += val;
            }
        }
        hardTotal = softTotal + aces;
        if (aces > 0) {
            int remainder = 21 - softTotal;
            int numHigh = remainder/11;
            aces -= numHigh;
            softTotal += (aces + numHigh * 11);
        }


//        for (HashMap.Entry<Integer, Double> entry : availableCards.entrySet()) {
//            Integer key = entry.getKey();
//            Double value = entry.getValue();
//            System.out.printf("Key: %d   Value: %,.4f\n", key, value);
//        }
        logger.log(Level.INFO, String.format("Soft total: %d   Hard total: %d", softTotal, hardTotal));
        return softTotal < 17;
    }
}
