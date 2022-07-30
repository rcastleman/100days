from question_model import Question
from data import new_question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range (len(new_question_data)):
    question = Question(new_question_data[i]["question"],new_question_data[i]["correct_answer"])
    question_bank.append(question)

# for element in question_bank:
#     print(element.__dict__)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")