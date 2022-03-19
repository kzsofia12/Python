#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


letter = ""
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()


for i in range(len(names)):
    names[i] = names[i].strip('\n')
    with open(f"./Output/ReadyToSend/invented_{names[i]}.txt", mode="w") as file:
        full = letter.replace("[name]", names[i])
        file.write(full)
