"""
Manual scoring tests for specific hands

To run from repo root (with venv active):
    python tests/manual_scoring.py
"""

from blackjack.scoring import hand_value
from blackjack.cards import Card


def make_hand(ranks, suit="♠"):
    """Helper: build a hand from ranks (suits don't matter yet)."""
    return [Card(rank, suit) for rank in ranks]

def run_case(name, ranks, expected):
    hand = make_hand(ranks)
    actual = hand_value(hand)
    passed = actual == expected
    
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}: ranks={ranks} expected={expected} actual={actual}")

    return passed

def main():
    # Add/adjust cases as you implement logic in scoring.py
    cases = [
        # No aces
        ("10 + 7", ["10", "7"], 17),
        ("K + 9", ["K", "9"], 19),

        # One ace
        ("A + 9", ["A", "9"], 20),
        ("A + K", ["A", "K"], 21),

        # Multiple aces
        ("A + A + 9", ["A", "A", "9"], 21),
        ("A + A + 9 + 9", ["A", "A", "9", "9"], 20),
        ("A + A + A + 9", ["A", "A", "A", "9"], 12),

        # Bust-ish cases
        ("K + Q + 2", ["K", "Q", "2"], 22),
        ("A + 9 + K + 2", ["A", "9", "K", "2"], 22),  # ace can't save this one
    ]

    passed_all = True
    for name, ranks, expected in cases:
        if not run_case(name, ranks, expected):
            passed_all = False

    print("\nAll tests passed!" if passed_all else "\nSome tests failed.")
    raise SystemExit(0 if passed_all else 1)


if __name__ == "__main__":
    main()