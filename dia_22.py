import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Efecto Visual con Turtle")

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.hideturtle()

def get_color(i, total):
    hue = i / total
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1)]
    return r, g, b

for i in range(360):
    t.color(get_color(i, 360))
    t.circle(100)
    t.left(10)
screen.mainloop()