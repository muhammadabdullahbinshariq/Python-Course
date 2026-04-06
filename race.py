import turtle
import random

screen = turtle.Screen()
screen.setup(500, 400)
screen.bgcolor("Black")
colors = ["red", "blue", "green", "yellow", "orange"]
all_turtles = []

# Create the turtles and line them up
for i in range(0, 5):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + (i * 50))
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for t in all_turtles:
        # Move each turtle a random amount
        distance = random.randint(0, 10)
        t.forward(distance)
        
        # Check if a turtle crossed the finish line
        if t.xcor() > 300:
            is_race_on = False
            print(f"The {t.pencolor()} turtle is the winner!")

screen.exitonclick()