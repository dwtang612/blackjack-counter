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
