def prompt_player_action():
    """
    Asking the player if they want to hit or stand.
    Returns: 'hit' or 'stand'
    """
    print("-" * 40)
    action = input("Hit or stand? (h/s): ").strip().lower()
    if action in ("h", "hit"):
        return "hit"
    elif action in ("s", "stand"):
        return "stand"
    else:
        print("Invalid input. Please enter 'h' or 's'.")
        return prompt_player_action()
    
def prompt_play_again():
    print("-" * 40)
    answer = input("Play again? (y/n): ").strip().lower()
    if answer in ("y", "yes"):
        return True
    elif answer in ("n", "no"):
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return prompt_play_again()

def show_hand(owner, hand, hide_first=False):
    label = "Your hand" if owner == "Player" else f"{owner}'s hand"
    print(f"\n{label}:")
    display_cards = []
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            display_cards.append("??")
        else:
            display_cards.append(str(card))
    print("  " + " ".join(display_cards))

def show_hand_value(owner, hand, scoring):
    value = scoring.hand_value(hand)
    if owner == "Player":
        print(f"Your total: {value}")
    else:
        print(f"{owner}'s total: {value}")
