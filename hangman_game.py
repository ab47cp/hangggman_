import tkinter as tk
from tkinter import messagebox
import requests
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangggman Game")

        self.reset_game()

        # GUI Elements
        self.word_display = tk.StringVar()
        self.update_word_display()

        self.word_label = tk.Label(root, textvariable=self.word_display, font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.letter_entry = tk.Entry(root, font=("Helvetica", 24))
        self.letter_entry.pack(pady=20)
        
        self.guess_button = tk.Button(root, text="Guess", command=self.guess_letter, font=("Helvetica", 14))
        self.guess_button.pack(pady=20)

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.max_attempts - self.attempts}", font=("Helvetica", 14))
        self.attempts_label.pack(pady=20)

        self.restart_button = tk.Button(root, text="Restart", command=self.reset_game, font=("Helvetica", 14))
        self.restart_button.pack(pady=20)

    #to get unique word
    def fetch_random_word(self):
        try:
            response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            response.raise_for_status()
            word = response.json()[0]
            return word
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch word: {e}")
            self.root.destroy()

    def update_word_display(self):
        display = " ".join([letter if letter in self.guesses else "_" for letter in self.word])
        self.word_display.set(display)

    def guess_letter(self):
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if letter in self.guesses:
            messagebox.showerror("Invalid Input", "You have already guessed that letter.")
            return

        self.guesses.add(letter)

        if letter not in self.word:
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

        self.update_word_display()
        self.check_game_over()

    def check_game_over(self):
        if all(letter in self.guesses for letter in self.word):
            messagebox.showinfo("Hangggman", f"Congratulations! You guessed the word: {self.word}")
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Hangggman", f"Game Over! The word was: {self.word}")

    def reset_game(self):
        self.word = self.fetch_random_word()
        self.guesses = set()
        self.max_attempts = 6
        self.attempts = 0
        if hasattr(self, 'word_display'):
            self.update_word_display()
        if hasattr(self, 'attempts_label'):
            self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
