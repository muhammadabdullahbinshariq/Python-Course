import turtle

screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

board = [" "] * 9
player = "X"
line = turtle.Turtle()
line.hideturtle()
line.pensize(5)

def draw_grid():
    line.clear()
    line.color("black")
    for x in [-100, 100]:
        line.penup()
        line.goto(x, 300)
        line.pendown()
        line.goto(x, -300)
    for y in [-100, 100]:
        line.penup()
        line.goto(-300, y)
        line.pendown()
        line.goto(300, y)
    screen.update()

def reset_game(x, y):
    global board, player
    board = [" "] * 9
    player = "X"
    line.clear()
    draw_grid()
    screen.onclick(play)

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def play(x, y):
    global player
    col = int((x + 300) // 200)
    row = int((y + 300) // 200)
    index = col + (row * 3)

    if 0 <= index < 9 and board[index] == " ":
        board[index] = player
        cx = (col * 200) - 200
        cy = (row * 200) - 200
        
        if player == "X":
            line.color("blue")
            line.penup()
            line.goto(cx - 40, cy - 40)
            line.pendown()
            line.goto(cx + 40, cy + 40)
            line.penup()
            line.goto(cx - 40, cy + 40)
            line.pendown()
            line.goto(cx + 40, cy - 40)
            player = "O"
        else:
            line.color("orange")
            line.penup()
            line.goto(cx, cy - 50)
            line.pendown()
            line.circle(50)
            player = "X"
        
        screen.update()
        winner = check_winner()
        
        if winner or " " not in board:
            line.penup()
            line.goto(0, 0)
            line.color("black")
            text = f"PLAYER {winner} WINS!" if winner else "IT'S A DRAW!"
            line.write(text, align="center", font=("Arial", 25, "bold"))
            line.goto(0, -40)
            line.write("Click anywhere to Restart", align="center", font=("Arial", 15, "normal"))
            screen.onclick(reset_game)

draw_grid()
screen.onclick(play)
turtle.done()