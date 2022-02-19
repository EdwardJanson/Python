import random

NUMBERS = []

for number in range(1, 101):
  NUMBERS.append(number)

def guess_number(difficulty):
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5

  print(f"You have {attempts} remaining to guess the number.")

  while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == random_number:
      print(f"You win! The answer is {random_number}.")
    elif guess > random_number:
      print(f"Too high.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses. You lose.")
    elif guess < random_number:
      print(f"Too low.")
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses. You lose.")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
random_number = random.choice(NUMBERS)

guess_number(difficulty)
