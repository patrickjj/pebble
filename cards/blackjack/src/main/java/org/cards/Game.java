package org.cards;

import java.util.ArrayList;

public class Game {
    public Dealer dealer;
    public ArrayList<Player> players;
    public Game(int numPlayers, int numDecks) {
        dealer = new Dealer(numDecks);
        players = new ArrayList<Player>(numPlayers);
        for (int i = 0; i < numPlayers; i++) {
            players.add(new Player());
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
    }

}
