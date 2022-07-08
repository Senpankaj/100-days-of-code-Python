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









