# ImposterGame

ImposterGame is a lightweight terminal-based party game inspired by the social deduction word game where one or more players are secretly the imposter(s) while everyone else knows the secret word. The game is designed for small groups and runs entirely from the command line.

## Overview

This project is a Python implementation of a simple "Imposter Who?" style game:

- 3 to 15+ players can participate
- One player starts the round
- A secret word is chosen for each non-imposter player
- The imposter receives a hint instead of the real word
- Players describe their word without saying it directly
- After the round, everyone votes to identify the imposter
- The true imposter(s) and secret word are revealed at the end

## How it works

The flow of the game is handled in `main.py`:

1. A starting menu is shown
2. Players enter their names
3. The game determines the number of imposters
4. Random players are assigned as imposters
5. One player is selected to begin the round
6. Secret words and hints are assigned
7. The round is started and the word assignment is revealed at the end

## Features

- Terminal UI using JSON-defined modal menus
- Configurable min/max player count (`3` to `15`)
    - Don't change the lower the minimum- it will break the game
- Randomized word assignment and imposter selection
- Rotation-based turn order using random clockwise or counter-clockwise direction
- Built-in instructions menu
- Word dataset stored in `utilities/words.json`
    - Add your own!

## Requirements

- Python 3
- A real terminal environment

This project uses terminal screen control features (`sys.stdout.isatty()` and alternate screen rendering), so it works best when launched in a normal terminal session rather than a limited or non-interactive environment.

## Quick start

```bash
git clone https://github.com/dunccarr/impostergame.git
cd impostergame
python main.py
```

Replace `python` with `python3` for Mac and Linux.

## Playing the game

When the program starts:

- Choose `Begin Game` from the main menu
- Enter each player's name
- Set the number of imposters and player count as prompted
- Pass the device to each player as they receive their role
- Take turns describing your word without revealing it directly
- Vote at the end of the round to find the imposter

## Notes

- The words and hints are drawn from the JSON list in `utilities/words.json`
- The game is intentionally simple and meant to run locally with friends
- The project is a lightweight, script-based game rather than a graphical app

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
