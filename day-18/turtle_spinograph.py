from turtle import Turtle, Screen
from random import choice , randint

tim = Turtle()
tim.width(1)
tim.shape("turtle")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(5)


screen.exitonclick()
