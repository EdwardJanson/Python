rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

chosen_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if chosen_number < 0 or chosen_number >= 3:
  print("You chose a wrong number, you lose.")
else:
  if chosen_number == 0:
    print(rock)
  elif chosen_number == 1:
    print(paper)
  else:
    print(scissors)

  random_number = random.randint(0, 2)

  if random_number == 0:
    print(rock)
  elif random_number == 1:
    print(paper)
  else:
    print(scissors)

  chose_0 = ["It's a draw.", "You lose.", "You win."]
  chose_1 = ["You win.", "It's a draw.", "You lose."]
  chose_2 = ["You lose.", "You win.", "It's a draw."]
  map = [chose_0, chose_1, chose_2]

  print(map[chosen_number][random_number])
