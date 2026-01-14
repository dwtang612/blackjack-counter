from typing import List
from blackjack.cards import Card

RANK_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

def hand_value(hand: List[Card]) -> int:
    """
    Calculate the total value of a Blackjack hand.

    Aces are counted as 11 or 1, whichever produces the highest
    total that does not exceed 21. (soft hands scenario)
    """
    
    total = 0
    ace_count = 0
    
    for card in hand:
        if card.rank == 'A':
            ace_count += 1
        else:
            total += RANK_VALUES[card.rank]

    total += ace_count * 11

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def is_bust(hand) -> bool:
    """
    Returns True of the hand value exceeds 21
    """
    return hand_value(hand) > 21