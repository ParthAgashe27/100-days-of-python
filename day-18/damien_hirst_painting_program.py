import turtle as t
import random
#only use to extract colors from an image
# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

#colors extracted from image.jpg (modified to remove duplicates and colors that are too light)

colour_list = [(204, 165, 107), (155, 73, 46), (174, 154, 37), (51, 93, 124), (224, 201, 133), (139, 31, 20), (132, 163, 185), (201, 90, 69),
(46, 123, 86), (13, 100, 73), (70, 48, 39), (99, 72, 74), (147, 179, 146), (235, 175, 164), (163, 141, 158), (55, 46, 50),(184, 206, 171),
 (18, 85, 90), (147, 18, 22), (41, 56, 60)]

def draw_dot_painting():
    t.colormode(255)
    t.speed("fastest")
    t.penup()
    t.hideturtle()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)

    for dot_count in range(1, 101):
        t.dot(18, random.choice(colour_list))
        t.forward(50)

        if dot_count % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)
        

draw_dot_painting()

screen = t.Screen()
screen.exitonclick()
