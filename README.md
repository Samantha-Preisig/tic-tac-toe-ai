Author: Samantha Preisig (02/03/2022)

# Tic-Tac-Toe (3x3, 4x4, and 5x5)

Requirements:
 - Python version 3.x

NOTE: If python 2 is installed on the system, the user may have to use `python3` instead of `python`

## How to play:
### Run ttt.py
``` 
python ttt.py
```

### Initialize game mechanics with a series of user prompts
- Once ttt.py is running, the user will be prompted to provide input to set up desired size of game and efficiency and effectiveness of the bot's decision
- `Please enter size of Tic-Tac-Toe board [3, 4, or 5]:`
  - Determines the size of the tic-tac-toe board
  - Valid input:
    - '3': creates a 3x3 TTT board
    - '4': creates a 4x4 TTT board
    - '5': creates a 5x5 TTT board
  - NOTE: ttt.py assumes valid input is entered (extensive error-checking not implemented yet)
- `How do you want the bot to play? [m = minimax, a = alpha-beta]:`
  - Decides the algorithm the bot will use to make its decisions
  - Valid input:
    - 'm': minimax algorithm
    - 'a': minimax algorithm with alpha-beta pruning
  - NOTE: ttt.py assumes valid input is entered (extensive error-checking not implemented yet)
- `Enter maximum ply:`
  - Determines the maximum ply the bot can search to (using the algorithm decided in the previous user input)
  - Valid input: any positive integer
  - NOTE: ttt.py assumes valid input is entered (extensive error-checking not implemented yet)

### Playing a move
- To make a move, enter a number from 1 to board_size*board_size (i.e., the possible positions in a 3x3 TTT game is from 1 to 9)
- For example, in a 3x3 TTT game, if the player wanted to play the center square, they would enter '5'
- NOTE: the program assumes the user will enter a position within the position matrix (listed below). However, the program can handle when a player attempts to move to an occupied space

### Position matrix (for reference)
```
3x3 position matrix = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
4x4 position matrix = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
]
5x5 position matrix = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20
]
```

## Utilities
### Depth-limited search implementation using (1 minute) timeout feature:
- If the maximum search ply is large and the state space is large (4x4 and 5x5 TTT games), the bot has a maximum of 1 minute to search as deep as possible (aiming for maximum ply) using a given algorithm and will return the most recent 'best move' found

### Bot decision information
- Upon the bot making a decision and playing its turn, the following information is displayed:
  - Time taken for the bot to search and make move (in milliseconds)
  - The number of nodes the bot explored within the game tree to decide the move
  - The maximum ply reached in the given search
