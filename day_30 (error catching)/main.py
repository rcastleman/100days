# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
except:
    # print("There was an error")
    file = open("a_file.txt","w")