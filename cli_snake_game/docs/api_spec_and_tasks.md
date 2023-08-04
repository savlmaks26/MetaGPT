## Required Python third-party packages
```python
"""
curses==2.2
random==1.2.1
time==1.7
json==2.0.9
argparse==1.1
unittest==1.0.1
setuptools==57.4.0
"""
```

## Required Other language third-party packages
```python
"""
No third-party packages in other languages are required.
"""
```

## Full API spec
```python
"""
This is a command-line based game, hence there are no APIs involved.
"""
```

## Logic Analysis
```python
[
    ("main.py", "This is the main entry of the game. It creates a Game instance and starts the game."),
    ("game.py", "This file contains the Game class. It controls the game flow, including starting and ending the game, updating the game state, and drawing the game."),
    ("snake.py", "This file contains the Snake class. It handles the snake's movement, growth, and collision checking."),
    ("apple.py", "This file contains the Apple class. It generates a new position for the apple."),
    ("scoreboard.py", "This file contains the Scoreboard class. It loads and saves high scores, and updates the score."),
    ("tests.py", "This file contains unit tests for the game."),
    ("setup.py", "This file is used to package the game for easy installation.")
]
```

## Task list
```python
[
    "main.py",
    "game.py",
    "snake.py",
    "apple.py",
    "scoreboard.py",
    "tests.py",
    "setup.py"
]
```

## Shared Knowledge
```python
"""
The 'curses' library is used to create the command-line interface, handle user input, and update the game display.
The 'random' library is used to generate the position of the apple.
The 'time' library is used to control the game speed.
The 'json' library is used to store and load the high scores.
The 'argparse' library is used to handle command-line arguments for starting a new game or viewing high scores.
The 'unittest' library is used for testing.
The 'setuptools' library is used to package the game for easy installation.
"""
```

## Anything UNCLEAR
The requirement is clear to me. However, we need to ensure that all team members are familiar with the Python standard library and the third-party libraries we are going to use. We also need to make sure that everyone understands the game mechanics and the structure of the code.