## Original Requirements
The boss has asked for a command-line interface (CLI) snake game to be developed.

## Product Goals
```python
[
    "Create a simple, engaging CLI snake game",
    "Ensure the game is easy to install and run",
    "Provide a high-score tracking system"
]
```

## User Stories
```python
[
    "As a user, I want to be able to easily start a new game so that I can play quickly",
    "As a user, I want the game to be challenging so that I can be engaged",
    "As a user, I want to be able to see my high score so that I can track my progress",
    "As a user, I want the game to run smoothly without any lags so that I can have a seamless gaming experience",
    "As a user, I want to be able to quit the game at any time so that I can stop playing when I want"
]
```

## Competitive Analysis
```python
[
    "Python Snake Game: A simple CLI snake game with basic features",
    "CLI Snake: A more complex CLI snake game with additional features like power-ups",
    "Terminal Snake: A CLI snake game with a unique visual style",
    "ASCII Snake: A CLI snake game that uses ASCII art for its graphics",
    "Retro Snake: A CLI snake game with a retro aesthetic",
    "Advanced Snake: A CLI snake game with advanced features like multiplayer",
    "Classic Snake: A CLI snake game that aims to replicate the classic mobile game"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "Python Snake Game": [0.2, 0.4]
    "CLI Snake": [0.6, 0.5]
    "Terminal Snake": [0.4, 0.3]
    "ASCII Snake": [0.5, 0.6]
    "Retro Snake": [0.7, 0.4]
    "Advanced Snake": [0.8, 0.7]
    "Classic Snake": [0.3, 0.2]
    "Our Target Product": [0.5, 0.6]
```

## Requirement Analysis
The product should be a command-line interface snake game. The game should be engaging, easy to install and run, and include a high-score tracking system.

## Requirement Pool
```python
[
    ("Develop the basic game mechanics", "P0"),
    ("Implement a high-score tracking system", "P0"),
    ("Ensure the game is easy to install and run", "P0"),
    ("Create a visually appealing CLI interface", "P1"),
    ("Implement a system to increase game difficulty over time", "P2")
]
```

## UI Design draft
The game will be a command-line interface game. The game area will be a grid displayed in the terminal. The snake will be represented by a line of characters that grows in length as the game progresses. The apple will be represented by a single character. The high score will be displayed at the top of the game area.

## Anything UNCLEAR
There are no unclear points.