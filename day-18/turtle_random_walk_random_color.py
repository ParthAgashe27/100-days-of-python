from turtle import Turtle, Screen
from random import choice , randint



tim = Turtle()
tim.width(10)
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

def randomwalk(steps):
    for _ in range(steps):
        tim.color(random_color())
        tim.forward(20)
        tim.setheading(choice([0, 90, 180, 270]))
        

randomwalk(200)

screen = Screen()
screen.exitonclick()

