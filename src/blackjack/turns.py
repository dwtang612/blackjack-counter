from blackjack.cards import deal_card
import blackjack.scoring as scoring

def player_turn(deck, player_hand, ui):
    while True:
        ui.show_hand("Player", player_hand)
        ui.show_hand_value("Player", player_hand, scoring)

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