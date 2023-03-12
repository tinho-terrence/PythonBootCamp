from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
still_others = True
bid_record ={}
highest_bid = 0
highest_name ="" 
while still_others:
  name = input("What's you name?: ")
  bid = int(input("What's your bid?: "))
  bid_record[name]= bid
  if bid > highest_bid:
    highest_bid = bid
    highest_name = name
  #print(bid_record)
  more = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if more =="no":
    still_others = False
  else:
    clear()
print(f"The winner is {highest_name} with a bid of ${highest_bid}")
#print(name)
#print(bid)
#print(more)

