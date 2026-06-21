import game_data
import art
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(user_guess, followers_a, followers_b):
    """Take the user's guess and the followers counts and returns if they got it right. """
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

game_loop = True

current_score = 0

print(art.logo)

account_b = random.choice(game_data.data)

while game_loop == True:
    
    account_a = account_b
    account_b = random.choice(game_data.data)
    while account_a == account_b:
        account_b = random.choice(game_data.data)


    print(f"Compare A: {format_data(account_a)}\n {art.vs}\n  Against B: {format_data(account_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B':" ).lower()

    followers_a_count = account_a["follower_count"]
    followers_b_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, followers_a_count, followers_b_count)

    if is_correct:
        current_score += 1
        print(f"You're Right!! Current Score: {current_score}.")
       

    else:
        print(f"You're Wrong!! Final Score: {current_score}.")
        game_loop = False
        
    
