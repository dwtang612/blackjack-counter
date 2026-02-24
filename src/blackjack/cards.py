import random

# Valid card ranks and suits used to generate a standard 52-card deck
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♠", "♥", "♦", "♣"]

class Card:
    """Represents a single playing card with a rank and suit."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # Human-readable representation (e.g., '10♠')
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        # Developer-friendly representation for debugging
        return f"Card(rank={self.rank}, suit={self.suit})"
    
def create_deck(num_decks: int = 2):
    """Create and return a shoe of num_decks standard 52-card decks."""
    deck = []
    for _ in range(num_decks):
        for rank in RANKS:
            for suit in SUITS:
                deck.append(Card(rank, suit))
    return deck
    
def shuffle_deck(deck):
    """Shuffle the deck in place."""
    random.shuffle(deck)

def deal_card(deck):
    """Remove and return the top card from the deck."""
    if not deck:
        raise ValueError("Cannot deal from an empty deck")
    return deck.pop()
    
