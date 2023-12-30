package org.cards;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;



public class Game {
    private final Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);


    public Dealer dealer;
    public ArrayList<Player> players;
    public Game(int numPlayers, int numDecks) {
        logger.setLevel(Level.INFO);
        dealer = new Dealer(numDecks);
        players = new ArrayList<Player>(numPlayers);
        for (int i = 0; i < numPlayers; i++) {
            players.add(new Player(logger, i+1));
        }
    }

    public void play() {
        deal();
    }

    private void deal() {
        for (int i = 0; i < 2; i++) {
            for (Player player : players) {
                dealer.dealCard(player);
            }
            dealer.dealCard();
        }
        for (Player player : players) {
            while (player.hit(dealer.availableCardMap())) {
                logger.log(Level.INFO, String.format("  Player %o has hit", player.id));
                dealer.dealCard(player);
            }
        }
        while (dealer.hit()) {
            dealer.dealCard();
        }
    }

}
