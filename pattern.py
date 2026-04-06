import turtle

angle = 121 #(or 91 or 175)
length = 0
colours = ["Red", "Yellow", "Green", "Blue", "Violet", "Purple"]

t = turtle.Turtle()
turtle.Screen().bgcolor("Black")
t.speed(0) 

running = True
while running:
    for i in colours:
        t.pencolor(i)
        t.forward(length)
        t.left(angle)
        length += 1
        
        if length >= 400:
            running = False
            break 

turtle.done()
