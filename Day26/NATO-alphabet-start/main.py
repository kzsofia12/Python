import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_alphabet)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ")
    try:
        word_alphabet = [dict_alphabet[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet")
        generate_phonetic()
    else:
        print(word_alphabet)


generate_phonetic()
