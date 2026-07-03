import turtle as t
import random

screen = t.Screen()

def race():
    
    screen.setup(width=500, height=400)
    user_bet = screen.textinput("Turtle Race - Make Your Bet", "Which turtle will win the race? (red, blue, green, yellow, orange, purple): ").lower()

    colors = ["red", "blue", "green", "yellow", "orange", "purple"]

    all_turtles = []

    for i in range(0, 6):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-230, y=100 - i * 40)
        new_turtle.color(colors[i])
        all_turtles.append(new_turtle)

    is_race_on = False

    if user_bet:
        is_race_on = True
        if user_bet not in colors:
            print("Invalid bet! Please choose a color from the list.")
            is_race_on = False

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            else:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)

race()

while True:

    play_again = screen.textinput("Play Again?", "Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        screen.clearscreen()
        race()
    elif play_again.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

screen.exitonclick()
