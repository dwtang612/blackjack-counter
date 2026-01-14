def prompt_player_action():
    """
    Asking the player if they want to hit or stand.
    Returns: 'hit' or 'stand'
    """
    return input("Hit or stand? ").strip().lower()

def show_hand(owner, hand):
    print(f"\n{owner}'s hand:")
    cards_str = " ".join(str(card) for card in hand)
    print(f"  {cards_str}")

def show_hand_value(owner, hand, scoring):
    value = scoring.hand_value(hand)
    print(f"{owner}'s total: {value}")