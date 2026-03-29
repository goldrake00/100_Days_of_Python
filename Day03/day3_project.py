## DAY 3 PROJECT Treasure Island
## 28.03.2026
## ASCII Art can be updated from: https://ascii.co.uk/art
## Flow Chart game rules:
## https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

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
/______/______/______/______/______/______/______/______/______/______/[Marco__]
*******************************************************************************

      
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Write your code below this line 👇

decision_1 = input(
    'You are on a road.Do you want to go left or right? Type "L" or "R" '
).lower()
if decision_1 == "l":
    decision_2 = input("Do you want to swim or wait? S or W ").lower()
    if decision_2 == "s":
        print("game over")
    elif decision_2 == "w":
        decision_3 = input("Which door? RED, YELLOW, BLUE ").lower()
        if decision_3 == "red" or decision_3 == "blue":
            print("game over")
        elif decision_3 == "yellow":
            print("You Win!")
        else:
            print("invalid choice")
elif decision_1 == "r":
    print("Game Over")
else:
    print("invalid choice")