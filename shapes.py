import turtle
turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup(500, 500)
turtle.shape("turtle")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.pendown()
turtle.left(90)
for i in range(2):
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
for i in range(6):
    turtle.forward(100)
    turtle.right(60)
turtle.done()