import random
import tkinter as tk

window = tk.Tk()
window.title("Rock Paper Scissors Game")

window_width = 400
window_height = 380
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
window.config(bg="#f4f4f9")

computer_options = {"0": "Rock", "1": "Paper", "2": "Scissor"}

def button_disable():
    b_rock.config(state="disabled", bg="#d1d1d6")
    b_paper.config(state="disabled", bg="#d1d1d6")
    b_scissor.config(state="disabled", bg="#d1d1d6")

def reset_game():
    b_rock.config(state="active", bg="#ff9500")
    b_paper.config(state="active", bg="#34c759")
    b_scissor.config(state="active", bg="#007aff")
    player_choice_label.config(text="Player: ")
    computer_choice_label.config(text="Computer: ")
    result_label.config(text="Winner: ")

def play(player_move):
    comp_key = str(random.randint(0, 2))
    comp_move = computer_options[comp_key]
    
    player_choice_label.config(text=f"Player: {player_move}")
    computer_choice_label.config(text=f"Computer: {comp_move}")
    
    if player_move == comp_move:
        match_result = "Match Draw"
    elif (player_move == "Rock" and comp_move == "Scissor") or \
         (player_move == "Paper" and comp_move == "Rock") or \
         (player_move == "Scissor" and comp_move == "Paper"):
        match_result = "You Win!"
    else:
        match_result = "Computer Wins!"
        
    result_label.config(text=f"Result: {match_result}")
    button_disable()

title_label = tk.Label(window, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#1c1c1e")
title_label.pack(pady=15)

player_choice_label = tk.Label(window, text="Player: ", font=("Helvetica", 12), bg="#f4f4f9", fg="#3a3a3c")
player_choice_label.pack(pady=4)

computer_choice_label = tk.Label(window, text="Computer: ", font=("Helvetica", 12), bg="#f4f4f9", fg="#3a3a3c")
computer_choice_label.pack(pady=4)

result_label = tk.Label(window, text="Winner: ", font=("Helvetica", 14, "bold"), bg="#f4f4f9", fg="#5856d6")
result_label.pack(pady=15)

frame = tk.Frame(window, bg="#f4f4f9")
frame.pack(pady=15)

b_rock = tk.Button(frame, text="Rock", font=("Helvetica", 11, "bold"), width=9, height=2, bg="#ff9500", fg="white", activebackground="#cc7600", activeforeground="white", relief="flat", command=lambda: play("Rock"))
b_rock.grid(row=0, column=0, padx=8)

b_paper = tk.Button(frame, text="Paper", font=("Helvetica", 11, "bold"), width=9, height=2, bg="#34c759", fg="white", activebackground="#248a3d", activeforeground="white", relief="flat", command=lambda: play("Paper"))
b_paper.grid(row=0, column=1, padx=8)

b_scissor = tk.Button(frame, text="Scissor", font=("Helvetica", 11, "bold"), width=9, height=2, bg="#007aff", fg="white", activebackground="#005ec2", activeforeground="white", relief="flat", command=lambda: play("Scissor"))
b_scissor.grid(row=0, column=2, padx=8)

reset_btn = tk.Button(window, text="Reset Game", font=("Helvetica", 11), width=14, height=1, bg="#8e8e93", fg="white", activebackground="#636366", activeforeground="white", relief="flat", command=reset_game)
reset_btn.pack(pady=20)

window.mainloop()