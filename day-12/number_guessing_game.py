import random

# Global constants for the number of turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks the user's guess against the actual answer. Returns remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns
    


def set_difficulty():
    """Asks the user for difficulty and returns the number of allowed turns."""
    difficult_1 = True
    while difficult_1 is True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        
        if level == "easy":
            return EASY_LEVEL_TURNS
            
        elif level == "hard":
            return HARD_LEVEL_TURNS
            
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")
            
def game():
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    
    turns = set_difficulty()
    
    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            # Return exits the function entirely, stopping the game loop
            return
        elif guess != answer:
            print("Guess again.")

# Start the game
game()
