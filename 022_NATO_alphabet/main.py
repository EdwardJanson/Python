import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = data.to_dict()
letter_data_frame = pandas.DataFrame(letter_dict)
ordered_dict = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}

input_l = input("Type the word you would like to have in phonetic code. ")
input_l_list = list(input_l)

phonetic_code = []

for l in input_l_list:
    phonetic_code += [code for (letter, code) in ordered_dict.items() if letter.lower() == l]

print(phonetic_code)
