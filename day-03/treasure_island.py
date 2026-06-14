print("Welcome to the Treasure Adventure!")
print("Your mission is to find the treasure.")
print("you're at a cross road. Where do you want to go? Type 'left' or 'right'")
cross_road = input().lower()
if cross_road == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    lake = input().lower()
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door = input().lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You chose a door that has a wise old man. He offered you a choice to choose between 'money' or 'wisdom'. Which one do you choose?")
            if input().lower() == "money":
                print("You chose money. The old man Smelled your greed and turned you into a frog. Game Over.")
            else:                
                print("You chose wisdom. The old man was impressed and gave you the treasure. You Win!")
        else:
                print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You tried to swim in a lake full of crocodiles. Game Over.")
else:
    print("You got kidnapped by a group of pirates. and you were tied up to a ship , you have a dull knife in your pocket, you can try to cut the rope and escape. Type 'cut' to cut the rope or 'wait' to wait for the pirates to leave.") 
    response = input().lower()
    if response == "cut":
        print("You cut the rope and escaped, but you got caught by the pirates u have a choice to use the dull knife to fight the pirates or reach for sharp weapon nearby . Type 'fight with dull knife' to fight the pirates with dull knife or 'reach for sharp weapon' to fight with sharp weapon.")
        fight_response = input().lower()
        if fight_response == "fight with dull knife":
            print("You fought bravely with the dull knife, but the pirates overpowered you. Game Over.")
        elif fight_response == "reach for sharp weapon":
            print("You reached for the sharp weapon and fought the pirates. You Win!")
    else:
        print("You waited for the pirates to leave, but they came back and found you useless. They threw you into the sea. Game Over.")
