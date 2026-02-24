from blackjack.cards import create_deck, deal_card, shuffle_deck
from blackjack import ui, turns
import blackjack.scoring as scoring

def main() -> None:
    print("Blackjack Starting... \n")

    while True:
        print("\n" + "#" * 40)
        deck = create_deck()
        shuffle_deck(deck)

        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        ui.show_hand("Dealer", dealer_hand, hide_first=True)
        ui.show_hand("Player", player_hand)
        ui.show_hand_value("Player", player_hand, scoring)

        # Check for natural blackjack
        if scoring.hand_value(player_hand) == 21:
            if scoring.hand_value(dealer_hand) == 21:
                print("\nBoth have Blackjack! Push.")
            else:
                print("\nBlackjack! Player wins!")
            print("\nGame Complete.")
            if not ui.prompt_play_again():
                break
            continue

        player_result = turns.player_turn(deck, player_hand, ui)

        if player_result["bust"]:
            print("\nPlayer busts. Dealer wins!")
        else:
            dealer_result = turns.dealer_turn(deck, dealer_hand, ui)

            if dealer_result["bust"]:
                print("\nDealer busts. Player wins!")
            else:
                outcome = scoring.determine_outcome(
                    scoring.hand_value(player_hand),
                    dealer_result["value"]
                )
                if outcome == "win":
                    print("\nPlayer wins!")
                elif outcome == "lose":
                    print("\nDealer wins!")
                else:
                    print("\nPush! It's a tie.")

        print("\nGame Complete.")

        if not ui.prompt_play_again():
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()