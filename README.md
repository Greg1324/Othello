# Title: Othello Game

## Project Description
This is an implementation of the classic board game Othello (also known as Reversi). This project demonstrates game mechanics, including player input, game state management, and AI functionality.

## Features
- Play against an AI with strategic decision-making capabilities.
- Handles invalid moves and displays game status.
- Simple command-line interface for gameplay.

## Installation
To run Othello, all you need is Python installed on your machine. After cloning the repository, it can be played through your machine's command line interface.

## How to Use
The game starts by asking the user to choose a color. Black goes first and white goes second, with black being represented by X and white being represented by O.
The human player and AI are initialized based on the chosen color.

Game Loop:
The game alternates turns between the human player and the AI.
The human player inputs their move (make sure to enter the coordinate in this format: 1, 1).
The AI calculates and makes its move.
The game board is printed after each move, and the game continues until there are no valid moves left.
The winner will have most pieces left on the board at the end of the game.
