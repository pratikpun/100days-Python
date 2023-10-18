student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
numOfStudents = 0
for student in student_heights:
    sum += student
    numOfStudents += 1
print(sum)
print(numOfStudents)
print(round(sum / numOfStudents))
