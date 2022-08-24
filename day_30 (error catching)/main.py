# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# except:
#     file = open("a_file.txt","w")
#     file.write("something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise KeyError

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError ("Human height < 3m")

bmi = weight / height **2
print(bmi)
