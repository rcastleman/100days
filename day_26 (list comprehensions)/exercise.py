import random

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

scores = {student:random.randint(1,100) for student in names}

# print(scores)

passed = {student:score for (student,score) in scores.items() if score >= 60}

print(passed)
