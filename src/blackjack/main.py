from blackjack.cards import create_deck, deal_card, shuffle_deck
from blackjack import ui, turns
import blackjack.scoring as scoring
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
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Show initial state (Dealer hand hidden)
    ui.show_hand("Player", player_hand)
    ui.show_hand_value("Player", player_hand, scoring)
    ui.show_hand("Dealer", dealer_hand, hide_first=True)

    player_result = turns.player_turn(deck, player_hand, ui)

    if player_result["bust"]:
        print("\nPlayer busts.")
        return

    # Dealer plays only if player didn't bust
    dealer_result = turns.dealer_turn(deck, dealer_hand, ui)

    if dealer_result["bust"]:
        print("\nDealer busts. (Outcome resolution comes in Sprint 5)")
    else:
        print("\nDealer stands. (Outcome resolution comes in Sprint 5)")
    print("Game Complete.")


if __name__ == "__main__":
    main()