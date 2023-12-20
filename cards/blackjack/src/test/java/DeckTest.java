import org.junit.Test;
import org.cards.Deck;
import org.cards.Dealer;

public class DeckTest {
    @Test
    public void deckTest() {
        Deck deck = new Deck(2);
        deck.shuffle();
        System.out.println(deck.toString());
    }

    @Test
    public void dealerTest() {
        Dealer dealer = new Dealer(2);
    }
}
