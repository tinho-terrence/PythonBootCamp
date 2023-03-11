#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = 1+0.01*float(input("What percentage top would you like to give? "))
no_of_ppl = float(input("How many people to split the bill? "))
payment_each = round(total_bill/no_of_ppl*tip_percent, 2)
payment_each = '{:.2f}'.format(payment_each)
print(f"Each person should pay: ${payment_each}")