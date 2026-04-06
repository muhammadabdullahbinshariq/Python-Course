BLUE = '\033[94m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
ENDC = '\033[0m'

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def format_cell(cell):
    if cell == "X": return f"{BLUE}X{ENDC}"
    if cell == "O": return f"{YELLOW}O{ENDC}"
    return " "

def board():
    print(f"\n   1   2   3 ")
    print(f"1  {format_cell(row1[0])} | {format_cell(row1[1])} | {format_cell(row1[2])} ")
    print("  -----------")
    print(f"2  {format_cell(row2[0])} | {format_cell(row2[1])} | {format_cell(row2[2])} ")
    print("  -----------")
    print(f"3  {format_cell(row3[0])} | {format_cell(row3[1])} | {format_cell(row3[2])} ")

CurrentPlayer = "X"

while True:
    board()
    color = BLUE if CurrentPlayer == "X" else YELLOW
    print(f"\nTURN OF: PLAYER {color}{CurrentPlayer}{ENDC}")
    
    try:
        r = int(input("Row (1-3): "))
        c = int(input("Column (1-3): ")) - 1
    except ValueError:
        print("Use numbers 1, 2, or 3.")
        continue

    if r < 1 or r > 3 or c < 0 or c > 2:
        print("\nInvalid input.")
        continue

    placed = False
    target_row = [None, row1, row2, row3][r]
    if target_row[c] == " ":
        target_row[c] = CurrentPlayer
        placed = True

    if not placed:
        print("\nThis box is currently filled!")
        continue

    winner = None
    if row1[0] == row1[1] == row1[2] != " ": winner = row1[0]
    elif row2[0] == row2[1] == row2[2] != " ": winner = row2[0]
    elif row3[0] == row3[1] == row3[2] != " ": winner = row3[0]
    elif row1[0] == row2[0] == row3[0] != " ": winner = row1[0]
    elif row1[1] == row2[1] == row3[1] != " ": winner = row1[1]
    elif row1[2] == row2[2] == row3[2] != " ": winner = row1[2]
    elif row1[0] == row2[1] == row3[2] != " ": winner = row1[0]
    elif row1[2] == row2[1] == row3[0] != " ": winner = row1[2]

    if winner:
        board()
        win_color = BLUE if winner == "X" else YELLOW
        print(f"\n{win_color}CONGRATULATIONS! PLAYER {winner} WINS!{ENDC}")
        again = input("\nDo you want to play again? (y/n)")
        if again == 'y':
            print("Restarting...")
        else:
            break

    if " " not in row1 and " " not in row2 and " " not in row3:
        board()
        print("\nIT'S A DRAW!")
        again = input("\nDo you want to play again? (y/n)")
        if again == 'y':
            print("Restarting...")
            continue
        else:
            break

    CurrentPlayer = "O" if CurrentPlayer == "X" else "X"