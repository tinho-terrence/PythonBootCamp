#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def attempts_remain():
  global attempt
  if attempt == 0:
    print("You've run out of guesses, you lose.")
    return False
    
  else:
    print("Guess again.")
    print(f"You have {attempt} attempts remaining to guess the number.")  
    return True

game_on = True
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betwee 1 and 100.")

answer = random.randint(1,100)

print(f"pssst, the correct answer is {answer}")

difficulty = input("Choose difficulty. Type 'easy' or 'hard':")

if difficulty == "hard":
  attempt = 5
else:
  attempt = 10

print(f"You have {attempt} attempt remaining to guess the number.")

while game_on:
  guess_no = int(input("Make a guess: "))
  
  attempt -= 1
  if guess_no == answer:
    print(f"You got it! The answer is {answer}.")
    game_on = False
    
  elif guess_no > answer:
    print("Too high.")
    game_on = attempts_remain()
  
  elif guess_no < answer:
    print("Too low.")
    game_on = attempts_remain()

