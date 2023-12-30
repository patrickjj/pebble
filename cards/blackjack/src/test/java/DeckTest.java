import org.cards.*;
import org.junit.Test;

import java.util.ArrayList;

public class DeckTest {
    @Test
    public void deckTest() {
        Deck deck = new Deck(2);
        deck.shuffle();
        System.out.println(deck.toString());
    }

    @Test
    public void dealerTest() {
        int numPlayers = 3;
        Dealer dealer = new Dealer(2);
        ArrayList<Player> players = new ArrayList<Player>(numPlayers);
        for (int i = 0; i < numPlayers; i++) {
            players.add(new Player(null, i+1));
        }
        for (Player player : players) {
            dealer.dealCard(player);
        }
        for (Player player : players) {
            for (Card card : player.cards) {
                assert card != null;
            }
        }
    }

    @Test
    public void dealTest() {
        Game game = new Game(5, 8);
        game.play();

        for (Player player: game.players) {
            System.out.println(player.id);
            for (Card card : player.cards) {
                System.out.println(card);
                assert card != null;

            }
            System.out.println();
        }
        for (Card card : game.dealer.cards) {
            System.out.println(card);
            assert card != null;
        }
    }
}
