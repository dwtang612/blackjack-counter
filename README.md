# BlackJack-Counter

    to run this - ls into src directory and python -m blackjack.main

    Rules:
    • Dealer hits on 16, stands on 17 (choose soft-17 rule now)
    • Blackjack detection yes/no (choose now)
    • No betting for v1

    main.py — Orchestration only
        Responsibilities
            • Start the program
            • Call setup functions
            • Control round flow
            • Handle replay loop
            • Catch top-level exceptions
        Should NOT
            • Contain card math
            • Print individual cards
            • Compute scores

    cards.py — Domain model
        Responsibilities
            • Define ranks and suits
            • Create and shuffle deck
            • Deal cards
        Should NOT
            • Ask for user input
            • Decide winners
            • Print UI text
            • This file should be mostly pure logic.

    scoring.py — Rules & math
        Responsibilities
            • Convert hands → totals
            • Handle ace logic
            • Detect blackjack / bust
        Should NOT
            • Print anything
            • Modify game flow

    turns.py — Turn mechanics
        Responsibilities
            • Player hit/stand loop
            • Dealer behavior rules
            • Bust detection during turns
        Should NOT
            • Decide final outcome
            • Track stats

    ui.py — All I/O lives here
        Responsibilities
            • Printing hands
            • Prompting input
            • Formatting output
            • Displaying results
        Should NOT
            • Calculate scores
            • Decide rules
