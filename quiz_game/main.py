from question_model import Question
from data import question_data

question_bank = []

for i in range (len(question_data)):
    question = Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question)

for element in question_bank:
    print(element.__dict__)