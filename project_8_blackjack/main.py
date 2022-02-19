import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = []
player_cards = []
dealer_score = []
player_score = []

def draw_two(player, score):
  first_card = random.choice(cards)
  player.append(first_card)
  second_card = random.choice(cards)
  
  if first_card > 10 and second_card > 10:
    second_card = 1
  player.append(second_card)
  score.append(sum(player))

def add_card(player, score):
  additional_card = random.choice(cards)
  if score[0] > 10 and additional_card > 10:
    additional_card = 1
  player.append(additional_card)
  score[0] = sum(player)
  if 11 in player and score[0] > 21:
    for card in range(len(player)):
      if player[card] == 11:
        player[card] = 1
    score[0] = sum(player)

game_continues = True

while game_continues:
  dealer_cards.clear()
  player_cards.clear()
  dealer_score.clear()
  player_score.clear()
  
  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")

  if play_game == "y":
    draw_two(player_cards, player_score)
    draw_two(dealer_cards, dealer_score)
    print(f"   Your cards: {player_cards}, current {player_score[0]}\n   Computer's first card: {dealer_cards[0]}")

    pick_card = True
    next_card = "y"

    while pick_card:
      if player_score[0] < 22:
        if player_score[0] != 21 and next_card == "y":
          next_card = input("Type 'y' to get another card, type 'n' to pass: ")
          if next_card == "y":
            add_card(player_cards, player_score)
            if player_score[0] < 22:
              print(f"   Your cards: {player_cards}, current {player_score[0]}\n   Computer's first card: {dealer_cards[0]}")
            else:
              print(f"   Your final hand: {player_cards}, final score {player_score[0]}\n   Computer's final hand: {dealer_cards}, final score {dealer_score[0]}\nYou went over 21, you lose.")
        else:
          while dealer_score[0] < 17:
            add_card(dealer_cards, dealer_score)
          print(f"   Your final hand: {player_cards}, final score {player_score[0]}\n   Computer's final hand: {dealer_cards}, final score {dealer_score[0]}")
          if dealer_score[0] > 21:
            print("You win.")
          elif dealer_score[0] > player_score[0]:
            print("You lose.")
          elif player_score[0] > dealer_score[0]:
            print("You win.")
          else:
            print("It's a draw.")
          pick_card = False
      else:
        pick_card = False
  else:
    game_continues = False
    print("Thank you for playing. Goodbye.")
