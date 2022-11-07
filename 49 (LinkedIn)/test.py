
list = str([x for x in range(100)])

with open('test.txt',mode='w') as file:
    file.write(list)

