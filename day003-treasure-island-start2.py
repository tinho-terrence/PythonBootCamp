print('''
The Adventures of __
                 /_
  .-.           / utureGirl  _
   .'                in the / ) /|
   `._.-~.                   /   |
        .'                  (____|__st Century
__________________________________________________by JRO__

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("\n You wake up in an alley. There is a door at the end of the road.")

question1 = input("\n Do you wanna open it or go away? (Type 'open' or 'leave')\n").lower()
if question1 == "open":
  print("\n Now you opened the door. There is a guard taking a nap.")
  question2 = input("What would you do? Wake him up or sneak away? ('wake' or 'sneak')\n").lower()
  if question2 == "sneak":
    print("\n You passed the guard. You see a beatiful lady sleeping at the cetre of a grass field.")
    question3 = input("You can either kiss her, wake her up by calling, or wake her up by touching ('kiss', 'call' or 'touch')\n").lower()
    if question3 == "touch":
      print("\n You decided to touch her, as taking some advantage.")
      print("You realize you are doing some analyze even in a complete strange environment.")
      print("Suddenly you aware this is a dream.")
      print("Now you can choose to stay in the dream or not. You obtain the power of lucid dream. You win!")
    elif question3 == "kiss":
      print("\n This is poetic. She wake up. You stay in the dream. Game over.")
    elif question3 == "call":
      print("\n She wake up and turn into a beast. She ate you. You wake up from the dream. Game over.")
  elif question2 == "wake":
    print("\n 'You are not supposed to be here,' he said. He beat you till death.")
    print("You wake up from your dream. Game over.")
elif question1 == "leave":  
  print("\n You walked towards home. You go to work next morning. Everything stays the same.")
  print("Game over.")


   
