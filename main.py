import colorgram
import random

from turtle import Screen, Turtle

cursor = Turtle()
cursor.speed('fastest')
screen = Screen()
screen.colormode(255)


def get_colors(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors


color_list = get_colors('image.jpg', 50)[1:-2]

# Set starting point
cursor.penup()
cursor.setpos(-200, -200)


def paint_dot_row():
    for _ in range(10):
        cursor.dot(30, random.choice(color_list))
        cursor.penup()
        cursor.forward(50)


def move_up():
    cursor.setheading(90)
    cursor.forward(50)
    cursor.setheading(0)
    cursor.backward(500)


for _ in range(10):
    paint_dot_row()
    move_up()

screen.exitonclick()
