import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
hi = pandas.read_csv("nato_phonetic_alphabet.csv")
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in hi.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user = input("Enter any word: \n")

new_word = user.upper()

main_word = [nato_dict[key] for key in nato_dict if key in new_word]

print(main_word)
