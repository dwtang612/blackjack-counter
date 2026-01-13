import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♠", "♥", "♦", "♣"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit})"
    
def create_deck():
    deck = []
    
    for rank in RANKS:
        for suit in SUITS:
            deck.append(Card(rank, suit))
    return deck
    
def shuffle_deck(deck):
     random.shuffle(deck)

def deal_card(deck):
    if not deck:
        raise ValueError("Cannot deal from an empty deck")
    return deck.pop()
    
