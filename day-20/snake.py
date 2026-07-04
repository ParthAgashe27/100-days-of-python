from turtle import Turtle

Snake_move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=-20 * i, y=0)
            self.segments.append(new_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):     #loop through the segments in reverse order
            new_x = self.segments[segment_number - 1].xcor()            #get the x coordinate of the previous segment
            new_y = self.segments[segment_number - 1].ycor()            #get the y coordinate of the previous segment
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(Snake_move_distance)  # Move the head of the snake forward

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:    
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    
