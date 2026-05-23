# SWK Simulator

SWK Simulator is a terminal-based text adventure set around the Schöpfwerk area. The player makes numbered decisions, moves through several story branches, can visit a shop, play a small guessing game, fight in a simple turn-based combat system, and reach different endings.

The game text itself is written in German. This README is written in English to describe the project structure and how to run it.

## Features

- Interactive command-line story with numbered choices
- Multiple endings, including good, bad, and secret endings
- Player name input
- JSON savegame output
- Inventory updates through the shop system
- Item-specific story paths after buying a Döner, drink, or pocket knife
- Number guessing minigame
- Turn-based combat system with random damage
- Colored terminal output through `colorama`
- ASCII art for selected scenes
- Basic input validation for numeric choices

## Requirements

- Python 3
- `colorama`

No `requirements.txt` file is included yet, so install the dependency manually:

```powershell
python -m pip install colorama
```

Because the package directory is named `schöpfwerk_simulator`, use a terminal and editor that handle UTF-8 paths correctly.

## How to Run

Open a terminal in the project directory and start the game with:

```powershell
python main.py
```

Optional virtual environment setup on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install colorama
python main.py
```

## How to Play

1. Start the game with `python main.py`.
2. Enter a name for the savegame.
3. Enter the player name.
4. Read the story prompts carefully.
5. Answer choices by entering the listed numbers.
6. At the end, choose whether the latest saved result should be printed.

Most inputs are numeric. If a non-number is entered, the game asks again. Some story branches treat unlisted numbers as a bad ending or exit path.

## Savegames

The game writes save data as a JSON file in the project root.

Example:

```text
my_save.json
```

The save file contains:

- `name`: player name
- `inventar`: current inventory
- `entscheidungen`: stored decisions, especially the ending
- `dateiname`: original savegame name

Using the same savegame name again overwrites the existing JSON file. JSON save files are ignored by Git through `.gitignore`.

Important: the save file stores the result of a run, but the current version does not load a previous savegame to continue from it. Starting `main.py` always begins a new run.

## Project Structure

```text
SWK-SIMULATOR/
├── main.py
├── README.md
├── LICENSE
├── .gitignore
└── schöpfwerk_simulator/
    ├── global_variablen.py
    ├── speichern.py
    ├── errors/
    │   └── error.py
    ├── story/
    │   ├── ASCII_ART.py
    │   ├── DukaufstDöner.py
    │   ├── DukaufstGetränk.py
    │   ├── DukaufstTaschenmesser.py
    │   ├── Kampfsystem.py
    │   ├── Story.py
    │   ├── Zahlenkontrolle.py
    │   ├── hauptteil.py
    │   ├── hauptteil_1_3.py
    │   ├── hauptteil_2.py
    │   ├── minigame.py
    │   ├── prolog.py
    │   ├── shop.py
    │   └── user.py
    └── texte/
        ├── text_formatieren.py
        └── texte.py
```

## Main Files

### `main.py`

Entry point of the game. It prints the title ASCII art, asks for a savegame name, initializes the global savegame name, starts the story, and optionally prints the last saved JSON result.

### `schöpfwerk_simulator/global_variablen.py`

Stores shared runtime state:

- current player name
- player inventory
- player decisions
- current savegame name

### `schöpfwerk_simulator/speichern.py`

Handles savegame writing and reading:

- `spielstand_speichern(...)` writes the current state to a `.json` file
- `read_json(...)` prints a saved JSON file

### `schöpfwerk_simulator/story/`

Contains the interactive story logic:

- `prolog.py`: opening scene
- `hauptteil.py`: main story path after the prologue
- `hauptteil_1_3.py`: branch for specific story decisions
- `hauptteil_2.py`: branch that unlocks minigame, shop, or final story
- `Story.py`: final story section without a special shop item
- `DukaufstDöner.py`, `DukaufstGetränk.py`, `DukaufstTaschenmesser.py`: final story variants after shop purchases
- `shop.py`: shop and inventory handling
- `minigame.py`: number guessing game
- `Kampfsystem.py`: turn-based combat
- `ASCII_ART.py`: ASCII drawings used in the terminal
- `user.py`: player name input
- `Zahlenkontrolle.py`: numeric input validation

### `schöpfwerk_simulator/texte/`

Stores longer story texts and formatting helpers:

- `texte.py`: reusable story text blocks
- `text_formatieren.py`: wraps long text to the current terminal width

## Gameplay Notes

- The combat system starts both the player and the opponent with 50 HP.
- Attacking deals random damage and also causes the player to receive random damage.
- Healing restores 5 HP.
- The minigame chooses a random number between 1 and 100.
- Some endings are saved immediately after the decision that causes them.
- The game uses global state for player data and savegame data.

## Known Limitations

- Save files cannot currently be loaded to continue a previous run.
- There is no automated test suite.
- There is no dependency file such as `requirements.txt`.
- Some invalid numeric choices are not handled uniformly across all branches.
- Several imports are unused in the current version of the code.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
