# file = open("my_file.txt")
# contents = file.read()
# print(f"\nThe contents are: '{contents}'")
# file.close()

#WITH obviates the need to close the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#OVERWRITE file:
# with open("my_file.txt",mode = 'w') as file:
#     file.write("some new text here ... ")


#APPEND to the file:
# with open("my_file.txt",mode = 'a') as file:
#     file.write("\n some new text here ... ")

with open("my_new_file.txt",mode = 'w') as file:
    file.write("some new tezt in a new file")
