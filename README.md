# Hangman Game with GUI

This is a Python implementation of the classic Hangman game with a graphical user interface (GUI) built using `tkinter`. 
The game fetches a random word from an online API to ensure a unique word each time the game is run.

## Features

- GUI for an interactive Hangman game experience
- Fetches a random word from an online API for each game
- Displays the number of attempts left
- Provides feedback on invalid inputs
- Restart button to play again without restarting the application

## Requirements

- Python 3.6 or higher
- `tkinter` (included with most standard Python installations)
- `requests` library

## Installation

1. *Clone the repository*:
   git clone https://github.com/your-username/hangman-game.git
   
   cd hangman-game

2. Install dependencies:
Optionally, you can create a virtual environment:

  - python3 -m venv venv
  - source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:

  - pip install -r requirements.txt

4. Usage
  Run the application:

  - python hangman_game.py
    
  Play the Game:

  - Enter a letter in the input field and click "Guess" to make a guess.
  - The game will display the word with underscores for unguessed letters and the number of attempts left.
  - The game will end when you guess the word or run out of attempts.
