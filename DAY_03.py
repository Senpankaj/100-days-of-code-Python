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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Tresure Island.')
print('Your mission is to find the treasure.')

first = input('You\'re at a cross road. Where do you want to go? type\"left\" or \"right\"')

if first == "right":
    second = input('You came to a lake. There is an island in the middle of the lake. Type \'wait\' to wait for the boat. Type \'swim\' to swim across.')
    if second == "swim":
        third = input('You arrived to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose ?')
        if third == "red":
            print('You have found tresure!')
        elif third == "yellow":
            print('Room is full of fire. Game Over.')
        elif third == "blue":
            print('Room is full of fire. Game Over.')
        else:
            print('You got attacked by an angry monster. GAME OVER')
    elif second == "wait":
        print('You made a wrong choice. GAME OVER')
    else:
        print('Tribel people got you. GAME OVER')
else:
    print('You made a wrong choice. GAME OVER')









