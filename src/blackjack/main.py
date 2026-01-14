from blackjack.cards import create_deck, deal_card, shuffle_deck
from blackjack import ui, turns
"""
Program entry point and high-level orchestration for the Blackjack CLI game.

Responsible for:
- Starting the Blackjack game
- Running a single game session
- Managing program-level flow
"""

def play_game() -> None:
    """Run a single Blackjack game session."""
    # # Deck Setup
    # deck = create_deck()
    # shuffle_deck(deck)
    # print("Deck size after create:", len(deck))

    # # Creating Hands
    # player_hand = []
    # dealer_hand = []

    # # Deal opening cards
    # for _ in range(2):
    #     player_hand.append(deal_card(deck))
    #     dealer_hand.append(deal_card(deck))

    # print("Deck size before dealing:", len(deck))
    
    # # Dislay Hands
    # print("\nPlayer Hand")
    # for card in player_hand:
    #     print(card)

    # print("\nDealer Hand")
    # for card in dealer_hand:
    #     print(card)
    pass

def main() -> None:
    """
    Application entry point.
    Keeps startup/shutdown behavior separate from game logic.
    """
    print("Backjack Starting... \n")
    # play_game()
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = [deal_card(deck), deal_card(deck)]

    result = turns.player_turn(deck, player_hand, ui)

    if result["bust"]:
        print("\nPlayer Busts")
    else:
        print("\n\nPlayer Stands")
    print("Game Complete.")


if __name__ == "__main__":
    main()