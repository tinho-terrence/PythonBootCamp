#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
from replit import clear
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the sum of cards"""
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(a, b):
  if a == b:
    return("Draw")
  elif a == 0:
    return("You got Black Jack. You win.")
  elif b == 0:
    return("Your opponent got Black Jace. You lose.")
  elif a > 21:
    return("Your brust. You lose.")
  elif b > 21:
    return ("You opponent brust. You win.")
  elif a > b:
    return ("You win.")
  else: 
    return ("You lose.")
    
def game():
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False
  print(logo)
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"player cards: {user_cards}, score: {user_score}")
    print(f"computer's first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score >21:
      is_game_over = True
      
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
      draw_card = input("do you wanna one more card? 'y' or 'n'") 
      if draw_card == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final cards: {user_cards} final score: {user_score}")
  print(f"Computer final cards: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you wanna another game? 'y' or 'n'") == "y":
  clear()
  game()
  
