def prompt_player_action():
    """
    Asking the player if they want to hit or stand.
    Returns: 'hit' or 'stand'
    """
    return input("Hit or stand? ").strip().lower()

def show_hand(owner, hand, hide_first=False):
    print(f"\n{owner}'s hand:")
    display_cards = []
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            display_cards.append("??")
        else:
            display_cards.append(str(card))
    print("  " + " ".join(display_cards))

def show_hand_value(owner, hand, scoring):
    value = scoring.hand_value(hand)
    print(f"{owner}'s total: {value}")