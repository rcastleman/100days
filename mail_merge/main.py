#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#DONE use readlines() on Invited Names to create list of names
with open("Input/Names/invited_names.txt") as file:
    raw_names = file.readlines()
    names = []
    for name in raw_names:
        name = name.replace("\n","")
        names.append(name)

for name in names: 
    with open("Input/Letters/starting_letter.txt") as text:
        text = text.readlines()
        text  = " ".join(text)
        text = text.replace("[name]",name)

    with open(f"Output/ReadyToSend/{name}_letter.txt",mode = "w") as new_letter:
        new_letter.write(text)
    