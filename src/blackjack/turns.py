from blackjack.cards import deal_card
import blackjack.scoring as scoring

def dealer_turn(deck, dealer_hand, ui) -> dict:
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
                "bust": True,
                "value": scoring.hand_value(dealer_hand),
            }
    return {
        "bust": False,
        "value": scoring.hand_value(dealer_hand),
        }



def player_turn(deck, player_hand, ui) -> dict:
    while True:
        if scoring.is_bust(player_hand):
            return {
                "bust": True,
            }

        action = ui.prompt_player_action()

        if action == "hit":
            player_hand.append(deal_card(deck))
            ui.show_hand("Player", player_hand)
            ui.show_hand_value("Player", player_hand, scoring) 
        elif action == "stand":
            return {
                "bust": False,
            }
        
