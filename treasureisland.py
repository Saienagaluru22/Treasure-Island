print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
option1 = input("You're at a crossroad, Cloud you like to go on right or left.? ").lower()
if option1 == "left":
    option2 = input("You have come to a lake. There is island in the middle of the lake. Wloud you like to wait for boat or you will go by swim.? ").lower()
    if option2 == "wait":
        option3 = input("Which door would you like to choose for the treasure red or yellow or blue.? ").lower()
        if option3 == "red":
            print("It's a room full of fire. Game Over!")
        elif option3 == "yellow" :
            print("You find the treasure.You Win!")
        elif option3 == "blue":
            print("It's a room full of water.Game Over!")
        else:
            print("You choose a door that doesn't exist.Game Over!")
    else:
         print("You choosen the worng option.Game Over!")
else:
    print("You choosen the worng option.Game Over!")