"""
Program entry point and high-level orchestration for the Blackjack CLI game.

Responsible for:
- Starting the Blackjack game
- Running a single game session
- Managing program-level flow
"""

def play_game() -> None:
    """Run a single Blackjack game session."""
    print("Playing one game of Blackjack ['♠', '♥', '♦', '♣']")

def main() -> None:
    """
    Application entry point.
    Keeps startup/shutdown behavior separate from game logic.
    """
    print("Backjack Starting...")
    play_game()
    print("Game Complete.")

if __name__ == "__main__":
    main()