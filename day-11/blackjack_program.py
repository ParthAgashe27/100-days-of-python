import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []
drawn_card_by_user_input = []
drawn_card_by_computer = []

program = True


while program == True:
    user_input_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if user_input_1 == "y":
        print(art.logo)
        user_cards = random.sample(cards, 2) 
        
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        computer_cards = random.sample(cards, k=1)
        

        print(f"Computer's first card: {computer_cards}")
    else:
        exit()
       

    hit_and_stand = True
    while hit_and_stand == True:
        user_input_2 = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_input_2 == "y":
            drawn_card_via_user_input = random.choice(cards)
            user_cards.append(drawn_card_via_user_input)
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\n Computer's first card: {computer_cards}")
            addition = sum(user_cards)
        
            if addition > 21:
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n Computer's final card: {computer_cards}, final score: {sum(computer_cards)}  ")
                print("You went over. You Lose!!")
                hit_and_stand = False
                break

                
        

        if user_input_2 == "n":
            while sum(computer_cards) <= 21:
                drawn_card_by_computer = random.choice(cards)
                computer_cards.append(drawn_card_by_computer)
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n Computer's final card: {computer_cards}, final score: {sum(computer_cards)}  ")

                if sum(computer_cards) > 21:
                    print("The computer went over. You Win!!")
                    hit_and_stand = False
                    break 

                elif sum(user_cards) < sum(computer_cards):
                    print("You Lose")
                    hit_and_stand = False
                    break 

                elif sum(computer_cards) == 21 and computer_cards == [10,11]:
                    print("Lose, The opponent has Blackjack!!")
                    hit_and_stand = False
                    break 

    
