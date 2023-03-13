from art import logo

#CAlculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add, 
   "-":subtract, 
   "*":multiply, 
   "/": divide
}

def cal():
  print(logo)
  
  finish_cal = False
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
    
  while not finish_cal:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1}{operation_symbol}{num2} = {answer}")
    yes_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if yes_no == "n":
      finish_cal = True
      cal()
    if yes_no =="y":
      num1 = answer
cal()