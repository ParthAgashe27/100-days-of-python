from turtle import Turtle, Screen
from random import choice

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

tim = Turtle()
tim.width(10)
tim.shape("turtle")
tim.speed("fastest")
def randomwalk(steps):
    for _ in range(steps):
        tim.color(choice(colors))
        tim.forward(20)
        tim.setheading(choice([0, 90, 180, 270]))
        

randomwalk(200)

screen = Screen()
screen.exitonclick()

