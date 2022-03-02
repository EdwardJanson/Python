with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_lines = letter.readlines()

with open("./Input/Names/invited_names.txt", "r") as names:
    name_list_raw = names.readlines()

name_list = []

for name in name_list_raw:
    name_list.append(name.strip("\n"))


def write_letter():
    for name_clean in name_list:
        with open(f"./Output/ReadyToSend/letter_for_{name_clean}.txt", "w") as new_letter:
            new_letter.write("".join(letter_lines))
        with open(f"./Output/ReadyToSend/letter_for_{name_clean}.txt", "r") as new_letter:
            letter_content = new_letter.read()
            letter_content = letter_content.replace("[name]", f"{name_clean}")
        with open(f"./Output/ReadyToSend/letter_for_{name_clean}.txt", "w") as new_letter:
            new_letter.write(letter_content)

write_letter()
