import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import math

# --- Configuration ---
COLOR_BG = "#000000"
COLOR_O = "#3498db"
COLOR_X = "#e74c3c"
COLOR_TAN = "#d2b48c"
COLOR_WIN = "#2ecc71"  # Vibrant Green for the winning line
FIREWORK_COLORS = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff", "#ffffff"]

board = [""] * 9
current_player = "O"
particles = []

class FireworkParticle:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+3, y+3, fill=color, outline="")
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifespan = random.randint(20, 40)

    def update(self):
        self.canvas.move(self.id, self.vx, self.vy)
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.canvas.delete(self.id)
            return False
        return True

def animate_fireworks(canvas):
    global particles
    particles = [p for p in particles if p.update()]
    if particles:
        wn.after(30, lambda: animate_fireworks(canvas))

def trigger_fireworks(canvas, combo):
    global particles
    for idx in combo:
        r, c = idx // 3, idx % 3
        x, y = c * 105 + 52, r * 105 + 52
        color = random.choice(FIREWORK_COLORS)
        for _ in range(30):
            particles.append(FireworkParticle(canvas, x, y, color))
    animate_fireworks(canvas)

# --- NEW: Function to draw the Green Line ---
def draw_winning_line(canvas, combo):
    coords = []
    for idx in combo:
        r, c = idx // 3, idx % 3
        coords.extend([c * 105 + 52, r * 105 + 52])
    # The line is drawn using COLOR_WIN (Green)
    canvas.create_line(*coords, fill=COLOR_WIN, width=10, capstyle="round", smooth=True)

def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return combo
    return "Draw" if "" not in board else None

def handle_click(idx, btn_id, canvas):
    global current_player
    if board[idx] == "":
        board[idx] = current_player
        color = COLOR_O if current_player == "O" else COLOR_X
        r, c = idx // 3, idx % 3
        x, y = c * 105 + 52, r * 105 + 52
        
        canvas.delete(btn_id)
        canvas.create_text(x, y, text=current_player, font=("Arial", 40, "bold"), fill=color)
        
        result = check_winner()
        if result:
            if result != "Draw":
                draw_winning_line(canvas, result) # Draws the green line
                trigger_fireworks(canvas, result)
                msg = f"Player {board[result[0]]} Wins!"
            else:
                msg = "It's a Draw!"
            wn.after(1000, lambda: [messagebox.showinfo("Game Over", msg), show_menu()])
            return
        current_player = "X" if current_player == "O" else "O"
        turn_lbl.config(text=f"Turn: {current_player}", fg=(COLOR_O if current_player == "O" else COLOR_X))

def show_menu():
    for w in wn.winfo_children(): w.destroy()
    wn.geometry("350x450")
    wn.configure(bg=COLOR_BG)
    
    # --- Start Page Image ---
    try:
        # Load your tic-tac-toe.jpg
        img = Image.open("tic-tac-toe.jpg").resize((350, 250))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(wn, image=photo, bg=COLOR_BG)
        img_label.image = photo  # Keep reference
        img_label.pack(pady=20)
    except:
        tk.Label(wn, text="TIC TAC TOE", font=("Arial", 30, "bold"), bg=COLOR_BG, fg="white").pack(pady=50)
    
    # --- Aligned Start Button ---
    btn = tk.Button(wn, text="START GAME", bg=COLOR_TAN, font=("Arial", 14, "bold"), 
                    command=start_game, padx=30, pady=15)
    # relx/rely 0.5 centers it perfectly
    btn.place(relx=0.5, rely=0.75, anchor="center")

def start_game():
    global board, current_player, turn_lbl
    for w in wn.winfo_children(): w.destroy()
    wn.geometry("350x500")
    wn.configure(bg=COLOR_BG)
    board = [""] * 9
    current_player = "O"
    
    turn_lbl = tk.Label(wn, text=f"Turn: {current_player}", font=("Arial", 20, "bold"), bg=COLOR_BG, fg=COLOR_O)
    turn_lbl.pack(pady=10)
    canvas = tk.Canvas(wn, width=315, height=315, bg=COLOR_BG, highlightthickness=0)
    canvas.pack(pady=10)

    for i in range(9):
        r, c = i // 3, i % 3
        btn = tk.Button(wn, text="", font=("Arial", 20), width=5, height=2)
        btn_id = canvas.create_window(c*105+52, r*105+52, window=btn)
        btn.config(command=lambda idx=i, bid=btn_id: handle_click(idx, bid, canvas))

wn = tk.Tk()
wn.title("Tic Tac Toe")
show_menu()
wn.mainloop()