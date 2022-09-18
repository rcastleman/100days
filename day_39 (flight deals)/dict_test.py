

test_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"",
    "key4":"value4"
}

output = {k:"TESTING" for k,v in test_dict.items() if v==""}

print(output)

