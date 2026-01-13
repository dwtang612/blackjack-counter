from blackjack.cards import create_deck, shuffle_deck, deal_card
"""
Program entry point and high-level orchestration for the Blackjack CLI game.

Responsible for:
- Starting the Blackjack game
- Running a single game session
- Managing program-level flow
"""

def play_game() -> None:
    """Run a single Blackjack game session."""
    # Deck Setup
    deck = create_deck()
    shuffle_deck(deck)
    print("Deck size after create:", len(deck))

    # Creating Hands
    player_hand = []
    dealer_hand = []

    # Deal opening cards
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    print("Deck size before dealing:", len(deck))
    
    # Dislay Hands
    print("\nPlayer Hand")
    for card in player_hand:
        print(card)

    print("\nDealer Hand")
    for card in dealer_hand:
        print(card)

def main() -> None:
    """
    Application entry point.
    Keeps startup/shutdown behavior separate from game logic.
    """
    print("Backjack Starting...")
    play_game()
    print("Game Complete.")


if __name__ == "__main__":
    main()