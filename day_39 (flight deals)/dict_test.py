

test_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"",
    "key4":"value4"
}

# for key, value in test_dict.items():
#     if value == "":
#         print(f"{key} has a null value")

test_dict = {k:"TESTING" for k,v in test_dict.items() if v==""}

print(test_dict)

