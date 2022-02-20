import random
import turtle
from turtle import Turtle, Screen

from setuptools._distutils.command.config import config

tim = Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed(5)
turtle.colormode(255)


# ----------Vẽ các khối đa giác đều
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(3,10):
#     timmy_turtle.color(random.choice(colors))
#     for y in range(i):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(360/i)

# --------Draw a Random Walk


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color


# direction = [0, 90, 180, 270]
# for i in range(100):
#     tim.color(random_color())
#     tim.forward(40)
#     tim.setheading(random.choice(direction))

# --------Draw Spirograph
def draw_spirograph(time):
    for i in range(time):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading((i + 1) * 360 / time)

tim.speed("fastest")
draw_spirograph(100)

screen = Screen()
screen.exitonclick()
