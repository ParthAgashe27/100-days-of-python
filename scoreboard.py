from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)
    
    def level(self):
        self.current_level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Gameover.", align="center", font=("Courier", 42, "normal"))
