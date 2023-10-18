import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract("painting.png", 10)


# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)

#     rgb_colors.append(new_color)

# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")

tim.penup()
tim.hideturtle()
color_list = [
    (188, 19, 46),
    (153, 87, 23),
    (188, 135, 35),
    (244, 233, 61),
    (252, 230, 236),
    (217, 238, 244),
    (195, 76, 34),
    (218, 66, 106),
    (15, 142, 89),
    (196, 176, 19),
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
