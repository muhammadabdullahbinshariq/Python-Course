import turtle
turtle.Screen().bgcolor("Orange")
sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("Welcome to Turtle!")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i += 1
turtle.done()