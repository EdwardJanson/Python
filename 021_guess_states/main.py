import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()

state_list_input = []
state_list = data["state"].to_list()

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(state_list_input)}/50 States Correct",
                                    prompt="What's another state name?")

    for state in state_list:
        if answer_state.lower() == state.lower() and answer_state.lower() not in state_list_input:
            state_list_input.append(answer_state)
            state_index = state_list.index(state)
            written_state = turtle.Turtle()
            written_state.hideturtle()
            written_state.penup()
            state_data = data[data.state == state]
            written_state.goto(int(state_data.x), int(state_data.y))
            written_state.write(f"{state}", align="center", font=("Arial", 10, "normal"))
    if len(state_list_input) > 49:
        winning_message = turtle.Turtle()
        winning_message.hideturtle()
        winning_message.write(f"You named all the states!", align="center", font=("Arial", 25, "normal"))
        game_is_on = False

screen.exitonclick()
