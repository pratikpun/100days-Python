import turtle as t
import random

tom = t.Turtle()

t.colormode(255)


# random color + random direction
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]
# tom.pensize(15)
# tom.speed(0)
# for _ in range(100):
#     tom.color(random_color())
#     tom.forward(30)
#     tom.setheading(random.choice(directions))

# Task 3, random colours
# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tom.width(5)
#         tom.forward(100)
#         tom.right(angle)

# Task 3, random colours + different shapes
# for shape_side in range(3, 9):
#     tom.color(random.choice(colours))
#     draw_shape(shape_side)


# Task 5, draw Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tom.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
