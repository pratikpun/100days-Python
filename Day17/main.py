from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


new_quizbrain = QuizBrain(question_bank)

new_quizbrain.next_question()

while new_quizbrain.still_has_questions():
    new_quizbrain.next_question()


print(f"Ypu've completed the quiz")
print(f"Your final score is {new_quizbrain.score} / {new_quizbrain.question_number}.")
