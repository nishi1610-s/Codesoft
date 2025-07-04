import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
comp_score = 0
winning_score = 0

# Choices
choices = ["stone", "paper", "scissor"]

# Function to determine winner of a round
def play(user_choice):
    global user_score, comp_score, winning_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "stone" and comp_choice == "scissor") or \
         (user_choice == "scissor" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "stone"):
        user_score += 1
        result = "You scored a point!"
    else:
        comp_score += 1
        result = "Computer scored a point!"

    # Update labels
    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer Score: {comp_score}")
    user_choice_label.config(text=f"You choose:{user_choice}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")
    result_label.config(text=result)

    # Check if someone won
    if user_score == winning_score:
        messagebox.showinfo("Game Over", f"You won the game by scoring {user_score} points!")
        root.destroy()
    elif comp_score == winning_score:
        messagebox.showinfo("Game Over", f"Computer won the game by scoring {comp_score} points!")
        root.destroy()

# Function to start the game
def start_game():
    global winning_score
    try:
        winning_score = int(entry.get())
        if winning_score <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")
        return

    start_frame.pack_forget()
    game_frame.pack()

# GUI Window
root = tk.Tk()
root.title("Stone Paper Scissor Game")
root.geometry("400x400")

# Start Frame
start_frame = tk.Frame(root)
start_frame.pack(pady=50)

tk.Label(start_frame, text="Enter points to win:", font=("Arial", 14)).pack()
entry = tk.Entry(start_frame, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(start_frame, text="Start Game", font=("Arial", 14), command=start_game).pack()

# Game Frame
game_frame = tk.Frame(root)

tk.Label(game_frame, text="Choose your move:", font=("Arial", 16)).pack(pady=10)

btn_frame = tk.Frame(game_frame)
btn_frame.pack()

tk.Button(btn_frame, text="Stone", font=("Arial", 12), width=10, command=lambda: play("stone")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissor", font=("Arial", 12), width=10, command=lambda: play("scissor")).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(game_frame, text="", font=("Arial", 14))
user_choice_label.pack(pady=10)

comp_choice_label = tk.Label(game_frame, text="", font=("Arial", 14))
comp_choice_label.pack(pady=10)

result_label = tk.Label(game_frame, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

user_score_label = tk.Label(game_frame, text="Your Score: 0", font=("Arial", 12))
user_score_label.pack()

comp_score_label = tk.Label(game_frame, text="Computer Score: 0", font=("Arial", 12))
comp_score_label.pack()

# Start main loop
root.mainloop()
