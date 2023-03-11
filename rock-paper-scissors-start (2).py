import random

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

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

print("Computer chose:")

pc_choice = random.randint(0,2)

if pc_choice == 0:
  print(rock)
elif pc_choice == 1:
  print(paper)
elif pc_choice == 2:
  print(scissors)

if choice == pc_choice:
  print("It's a draw")
elif (pc_choice == 1 and choice == 0) or (pc_choice == 2 and choice == 1) or (pc_choice == 0 and choice == 2):
  print("You lose")
elif (pc_choice == 0 and choice == 1) or (pc_choice == 1 and choice == 2) or (pc_choice == 2 and choice == 3):
  print("You win")