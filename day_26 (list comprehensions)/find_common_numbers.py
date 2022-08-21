
def process_file(file):
    with open(file) as file:
        nums = file.readlines()        
        num_list = [int(num.replace("\n","")) for num in nums]
    return num_list

list_1 = process_file("file1.txt")
list_2 = process_file("file2.txt")

# print(list_1)
# print(list_2)

result = [x for x in list_1 if x in list_2]

# print(result)

# Write your code above 👆

print(result)
