import turtle
import random
colors = ["red", "blue", "green", "yellow", "purple"]
start_x, start_y = -200, 100
turtles = []
for color in colors:
    t = turtle.Turtle()
    t.color(color), t.shape("turtle"), t.penup(), t.goto(start_x, start_y), t.pendown()
    turtles.append(t)
    start_y -= 50

line = turtle.Turtle()
line.penup(), line.goto(200, 150), line.pendown(), line.right(90)
line.forward(300)
race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= 200:
            race_on = False
            print(f"¡La tortuga {t.color()[0]} gana!")
            break

turtle.done()