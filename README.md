# Tic Tac Toe Game

## Description
This project implements the classic Tic Tac Toe game in Python, utilizing object-oriented programming. The game runs in the terminal and allows two players to compete against each other.

## Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/JuanPabloGomezHaroCabrera/Tic-tac-toe.git

## Navigate to the project directory
cd Tic-tac-toe

## Run the game
python Tic_tac_toe.py

## Usage
1. Start the game by running the tic_tac_toe.py script.
2. Follow the instructions in the terminal to input player moves.
3. The player who first completes a horizontal, vertical, or diagonal line with their marks (X or O) wins.
4. If the board is filled and there's no winner, the game ends in a draw.

## Project Structure
1. `Tic_tac_toe.py`: Contains the main function instantiating a game controller.
2. `GameController.py`: Class for managing the game, including players, the board, and scores.
3. `Player.py`: Class for information such as wins, mark, and a message to provide feedback for any invalid move.
4. `Board.py`: Class for board information, including cells, guide, and functions for understanding the state of the board.
5. `README.md`: Project documentation.

## Dependencies
This project uses the following standard Python libraries:

* `os`: For interacting with the operating system and clearing the terminal.
* `sys`: For quit the game.
* `time`: For introducing pauses in the game execution.