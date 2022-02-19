import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = ""
letter_guessed = input("Guess a letter between 'a' and 'z'.\n")
guess += letter_guessed.lower()
print(guess)

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
