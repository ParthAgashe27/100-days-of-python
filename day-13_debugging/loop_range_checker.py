#bug:used range(1, 20) so the print statement never went through
#fix: fixed the range to (1,21) 

def my_function():

    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
