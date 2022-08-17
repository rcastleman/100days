# file = open("my_file.txt")
# contents = file.read()
# print(f"\nThe contents are: '{contents}'")
# file.close()

#obviates the need to close the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
