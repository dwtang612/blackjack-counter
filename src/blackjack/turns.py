from blackjack.cards import deal_card
import blackjack.scoring as scoring

def dealer_turn(deck, dealer_hand, ui, reveal_delay=False) -> dict:
    """
    Dealer hits on 16 and stand on 17.
    Returns a dict smaller to player_turn
    """
    # Dealer shows full hand at the start of their turn
    ui.show_hand("Dealer", dealer_hand, hide_first=False)
    ui.show_hand_value("Dealer", dealer_hand, scoring)

    while scoring.hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

        ui.show_hand("Dealer", dealer_hand, hide_first=False)
        ui.show_hand_value("Dealer", dealer_hand, scoring)

        if scoring.is_bust(dealer_hand):
            return {
                "hand": dealer_hand,
                "bust": True,
                "stood": False,
                "value": scoring.hand_value(dealer_hand),
            }
    return {
        "hand": dealer_hand,
        "bust": False,
        "stood": True,
        "value": scoring.hand_value(dealer_hand),
        }



def player_turn(deck, player_hand, ui) -> dict:
    while True:
        if scoring.is_bust(player_hand):
            return {
                "hand": player_hand,
                "bust": True,
                "stood": False,
            }

        action = ui.prompt_player_action()

        if action == "hit":
            player_hand.append(deal_card(deck))
        elif action == "stand":
            return {
                "hand": player_hand,
                "bust": False,
                "stood": True,
            }
        
