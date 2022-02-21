import colorgram
import turtle
import random

colors = colorgram.extract("image.jpg", 30)
all_colors = []


def rgb_color(number):
    color = colors[number]
    rgb = color.rgb
    if rgb[0] > 235 and rgb[1] > 235 and rgb[2] > 235:
        return "white-ish"
    else:
        return rgb[0], rgb[1], rgb[2]


for color in range(len(colors)):
    color_tone = rgb_color(color)
    if color_tone != "white-ish":
        all_colors.append(color_tone)

spots = turtle.Turtle()
turtle.colormode(255)

y = -250
x = -250
spots.penup()
spots.setposition(x, y)

while y < 251 and x < 251:
    spots.pendown()
    spots.dot(20, random.choice(all_colors))
    spots.penup()
    spots.forward(50)
    x += 50
    if x > 250:
        x = -250
        y += 50
        spots.setposition(x, y)

screen = turtle.Screen()
screen.exitonclick()
