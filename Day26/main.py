# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_num = [num * num for num in numbers]

# print(numbers)

# print(squared_num)

# with open("file1.txt") as file1:
#     list1 = file1.readlines()


# with open("file2.txt") as file2:
#     list2 = file2.readlines()

# result = [int(num) for num in list1 if num in list2]

# print(result)
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Jack"]

# student_scores = {student: random.randint(1, 101) for student in names}

# print(student_scores)

# passed_students = {
#     student: score for (student, score) in student_scores.items() if score > 50
# }

# print(passed_students)

# input_sentence = "What is the Airspeed Velocity of an Unladen Swallow"

# list_of_words = input_sentence.split()

# result = {word: len(word) for word in list_of_words}

# print(result)

# weather_c = {
#     "Monday": 4,
#     "Tuesday": 5,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 20,
#     "Saturday": 22,
#     "Sunday": 19,
# }


# def temp_converter(temp_c):
#     return (temp_c * 9 / 5) + 32


# weather_f = {day: temp_converter(temp) for (day, temp) in weather_c.items()}


# print(weather_f)


student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# # Loop through dictionaries
# # for key, value in student_dict.items():
# #     print(value)

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through a data frame
# for key, value in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame

# for index, row in student_data_frame.iterrows():
#     print(student_data_frame)


# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetics_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
print(user_input)

for letter in user_input:
    print(letter)
output = [phonetics_dict[letter] for letter in user_input]
print(output)
