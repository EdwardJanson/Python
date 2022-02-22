from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

racer_colors = ["blue", "red", "orange", "green", "grey", "purple"]
racers = []

y = -125
racer_number = 0

for turtle in range(0, 6):
    racer = Turtle(shape="turtle")
    racers.append(racer)
    racer.penup()
    racer.pencolor(racer_colors[turtle])
    racer.color(racer_colors[turtle])
    racer.setposition(y=y, x=-200)
    racer_number += 1
    y += 50

race_is_still_on = True

while race_is_still_on:
    for racer in racers:
        random_number = random.randint(0, 10)
        racer.forward(random_number)
        if racer.xcor() >= 200:
            winner = racer
            race_is_still_on = False
            if racer.fillcolor() == user_bet:
                print("Your turtle won!")
            else:
                print("Your turtle lost.")

screen.exitonclick()
