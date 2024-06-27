#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    LETTER = letter.read()

with open("./Input/Names/invited_names.txt", "r") as name_list:
    NAME = name_list.readlines()


    for name in NAME:
        NEW_LETTER = LETTER.replace("[name]", name.strip())
        print(NEW_LETTER)
        with open(f"./Output/ReadyToSend/new_letter_{name.strip()}.txt", "w") as new_letter_file:
            new_letter_file.write(NEW_LETTER)