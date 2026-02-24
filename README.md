# Blackjack Counter

A command-line Blackjack game written in Python.  
This project is intentionally designed to review and practice core Python fundamentals,
not to overengineer a full casino simulator.

Concepts covered include:

- variables and data types
- lists, sets, and dictionaries
- functions and control flow
- classes and object usage
- exception handling
- modular project structure
- virtual environments

The goal is correctness, clarity, and learning.

---

## Running the Project

This project uses a Python virtual environment to isolate dependencies and avoid modifying
your global Python installation.

### Prerequisites

- Python 3.10 or newer
- macOS or Linux (Windows usage is similar)

---

## Setup (First Time Only)

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

This will:

- create a local virtual environment in .venv
- activate it for the current terminal session
- install the project in editable mode

---

## Running the Game

After activating the virtual environment:

```bash
python -m blackjack.main
```

---

## Re-activating the Environment (New Terminal)

Each time you open a new terminal session:

```bash
cd blackjack-counter
source .venv/bin/activate
python -m blackjack.main
```

To exit the virtual environment:

```bash
deactivate
```

---

## Game Rules (v1)

The following rules define the initial scope of the project:

- Standard 52-card deck
- Dealer hits on 16 and stands on 17
- Aces count as 11 unless doing so would bust the hand (then count as 1)
- Face cards (J, Q, K) count as 10
- No betting system in version 1
- Blackjack (natural 21) planned for a later sprint

---

## Project Structure

This project follows a real-world Python src layout.

```text
blackjack-counter/
├── src/
│   └── blackjack/
│       ├── __init__.py
│       ├── main.py
│       ├── cards.py
│       ├── scoring.py
│       ├── turns.py
│       └── ui.py
├── README.md
├── pyproject.toml
└── .gitignore
```

---

## Module Responsibilities

### main.py — Application Orchestration

Responsible for:

- Starting the application
- Coordinating overall game flow
- Managing round execution

Should NOT:

- Perform card math
- Compute hand scores
- Handle UI formatting

---

### cards.py — Card and Deck Logic

Responsible for:

- Defining card ranks and suits
- Representing individual cards
- Creating, shuffling, and dealing decks

Should NOT:

- Ask for user input
- Decide winners
- Print output

---

### scoring.py — Hand Scoring and Rules

Responsible for:

- Calculating hand totals
- Handling ace logic
- Detecting busts and blackjack

Should NOT:

- Print output
- Control game flow

---

### turns.py — Turn Mechanics

Responsible for:

- Player hit/stand loop
- Dealer behavior rules
- Bust detection during turns

Should NOT:

- Decide final outcomes
- Track statistics

---

### ui.py — Command-Line Interface

Responsible for:

- Displaying cards and hands
- Prompting user input
- Formatting output

Should NOT:

- Compute scores
- Decide game rules

---

## Edge Cases

### Handled
- **Ace logic** — Aces count as 11, but automatically drop to 1 if the hand would bust. Multiple aces are supported (e.g. A + A = 12, not 22).
- **Player bust** — Detected immediately after each hit; dealer turn is skipped.
- **Dealer bust** — Detected after each dealer hit; player wins automatically.
- **Push/tie** — Both hands equal; correctly resolved as a draw.
- **Dealer stands on soft 17** — Dealer hits on ≤16 and stands on ≥17, including soft hands.
- **Empty deck** — `deal_card()` raises a `ValueError` if the deck runs out of cards.
- **Invalid hit/stand input** — Only `h`, `hit`, `s`, `stand` accepted; re-prompts on anything else.
- **Invalid play again input** — Only `y`, `yes`, `n`, `no` accepted; re-prompts on anything else.
- **Natural blackjack** — If the player's opening two cards total 21, they win immediately without playing a turn.
- **Simultaneous blackjack** — If both player and dealer open with 21, it resolves as a push.
- **Statistics tracking** — Wins, losses, and pushes are tracked across rounds and displayed at end of session.

### Not Yet Handled
- **Deck exhaustion in long sessions** — A fresh deck is created each round, so running out mid-hand is not possible currently, but multi-deck support is not implemented.
- **Double down / split** — Not in scope for v1.

---

## Development Roadmap

- Sprint 0: Setup and rules definition
- Sprint 1: Deck and card modeling
- Sprint 2: Hand scoring logic
- Sprint 3: Player turn mechanics
- Sprint 4: Dealer logic
- Sprint 5: Outcome resolution
- Sprint 6: Multiple rounds and statistics
- Sprint 7: Input validation and error handling
- Sprint 8: Refactoring and polish

---

## License

This project is for learning and personal experimentation.
