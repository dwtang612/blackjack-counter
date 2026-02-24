from blackjack.cards import create_deck, deal_card, shuffle_deck
from blackjack import ui, turns
import blackjack.scoring as scoring

def main() -> None:
    print("Blackjack Starting... \n")

    stats = {"wins": 0, "losses": 0, "pushes": 0}
    try:
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
            player_natural = scoring.is_natural_blackjack(player_hand)
            dealer_natural = scoring.is_natural_blackjack(dealer_hand)

            if player_natural or dealer_natural:
                ui.show_hand("Dealer", dealer_hand, hide_first=False)
                if player_natural and dealer_natural:
                    print("\nBoth have Blackjack! Push.")
                    stats["pushes"] += 1
                elif player_natural:
                    print("\nBlackjack! Player wins!")
                    stats["wins"] += 1
                else:
                    print("\nDealer has Blackjack! Dealer wins.")
                    stats["losses"] += 1
                print("\nGame Complete.")
                if not ui.prompt_play_again():
                    break
                continue

            player_result = turns.player_turn(deck, player_hand, ui)

            if player_result["bust"]:
                print("\nPlayer busts. Dealer wins!")
                stats["losses"] += 1
            else:
                dealer_result = turns.dealer_turn(deck, dealer_hand, ui)

                if dealer_result["bust"]:
                    print("\nDealer busts. Player wins!")
                    stats["wins"] += 1
                else:
                    outcome = scoring.determine_outcome(
                        scoring.hand_value(player_hand),
                        dealer_result["value"]
                    )
                    if outcome == "win":
                        print("\nPlayer wins!")
                        stats["wins"] += 1
                    elif outcome == "lose":
                        print("\nDealer wins!")
                        stats["losses"] += 1
                    else:
                        print("\nPush! It's a tie.")
                        stats["pushes"] += 1

            print("\nGame Complete.")

            if not ui.prompt_play_again():
                break
    except KeyboardInterrupt:
        print("\n\nGame interrupted.")
    
    ui.show_stats(stats)
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()