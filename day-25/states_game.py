import pandas
import turtle


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


game_on = True

correct_guess = 0
number_of_states = len(all_states)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's the states name??").title()

while game_on == True:
    
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)
        correct_guess += 1
        all_states.remove(answer_state)
    elif answer_state == "Exit":

        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("states_to_learn.csv")

        break
        
    elif correct_guess == number_of_states:
        user_input = input("Would you like to take the quiz again. type 'y' is yes or 'n' if no??")
        if user_input == "y":
            game_on = True
            correct_guess = 0
        if user_input == "n":
            game_on = False
    
    
    answer_state = screen.textinput(title=f"Guesses {correct_guess}/{number_of_states}", prompt="What's the states name??").title()

        
screen.exitonclick()

