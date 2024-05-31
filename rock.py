import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    result_text = f"Player: {player_choice}\nComputer: {computer_choice}\n"
    
    if player_choice == computer_choice:
        result_text += "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_text += "You win!"
    else:
        result_text += "You lose!"
    
    result_label.config(text=result_text)

# Create the main application window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#2e2e2e")

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#2e2e2e", fg="#ffffff")
title_label.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#2e2e2e", fg="#ffffff")
result_label.pack(pady=20)

# Buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, text="Rock", font=("Arial", 14), bg="#f44336", fg="#ffffff", command=lambda: determine_winner("Rock"), height=2, width=10)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("Arial", 14), bg="#2196F3", fg="#ffffff", command=lambda: determine_winner("Paper"), height=2, width=10)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), bg="#4CAF50", fg="#ffffff", command=lambda: determine_winner("Scissors"), height=2, width=10)
scissors_button.pack(pady=10)

# Run the main application loop
root.mainloop()
