import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = data.to_dict()
letter_data_frame = pandas.DataFrame(letter_dict)
ordered_dict = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}

input_word = input("Type the word you would like to have in phonetic code. ").upper()
phonetic_code = [ordered_dict[letter] for letter in input_word]
print(phonetic_code)
