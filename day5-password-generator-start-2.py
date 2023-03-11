#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Eazy PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_pw = ""

for char in range(nr_letters):
  easy_pw += random.choice(letters)

for char in range(nr_symbols):
  easy_pw += random.choice(symbols)

for char in range(nr_numbers):
  easy_pw += random.choice(numbers)

print(easy_pw)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Welcome to the Hard PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

diff_pw = []

for char in range(nr_letters):
  diff_pw.append(random.choice(letters)) 

for char in range(nr_symbols):
  diff_pw.append(random.choice(symbols))

for char in range(nr_numbers):
  diff_pw.append(random.choice(numbers))

random.shuffle(diff_pw)

diff_pw_str = ""

for char in diff_pw:
  diff_pw_str += char

print(diff_pw_str)
