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

#TODO for Name in Invited Names

    #TODO create new letter 
        # using Open 
        # *in* the Output/ReadyToSend folder 
        # *and* give it proper filename

    #TODO replace [name] with Name
