from turtle import Turtle, Screen
from random import choice

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

tim = Turtle()
tim.shape("turtle")
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()

print(tim)
