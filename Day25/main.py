# # data = []

# # with open("weather_data.csv") as data_files:
# #     data = data_files.readlines()
# #     for index in data_from_file:
# #         data.append(index)
# #     print(data)

# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []

# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# # data_dict = data.to_dict()

# # temp_list = data["temp"].to_list()


# # print(data["temp"].max())

# # print(data[data.temp == data.temp.max()])

# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp * 9/5 + 32

# data_dict = {"students": ["Amy", "James", "Angle"], "scores": [76, 56, 65]}

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

### SQUIRREL TASK ###


# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# squirrel_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
# }

# df = pandas.DataFrame(squirrel_dict)
# df.to_csv("squirrel_dict.csv")

import turtle
import pandas


screen = turtle.Screen()

screen.title("U.S States GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


guessed_states = []

while len(guessed_states) < 50:
    # If answer_state is one of the states in all the states of the 50_states.csv
    # If it exists:
    # Create a turtle to write the the name of the state at the state's x and y corrodinates
    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / 50 States Correct",
        prompt="What's another state's name",
    ).title()

    # When game exit, make a list of missing answers by comparing guessed and full list, create a new csv with all the remaining answers
    if answer_state == "Exit":
        #     missing_states = []
        #     for state in states:
        #         if state not in guessed_states:
        #             missing_states.append(state)

        #     new_data = pandas.DataFrame(missing_states)

        ## using list comprehension
        missing_states = [
            missing_state
            for missing_state in states
            if missing_state not in guessed_states
        ]
        new_data = pandas.DataFrame(missing_states)

        new_data.to_csv("states_to_learn.csv")
        break
    # break

    # for every right answer, create a new turtle(word) in the coordinate provided in the csv
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))

        t.write(answer_state)
