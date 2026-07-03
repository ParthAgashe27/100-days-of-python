from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(50)

def move_backward():
    tim.backward(50)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.listen()
screen.exitonclick()
