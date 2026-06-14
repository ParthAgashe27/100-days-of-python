import art
print(art.logo)

data_of_bidder = {}
in_progress = True

# --- THE FUNCTION ---

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    bid_amount = bidding_record[name_of_bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name_of_bidder 
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# --- THE LOOP ---

while in_progress is True:

    name_of_bidder = input("What is your name?")
    bid_of_bidder = int(input("What amount would you like to bid?"))

    data_of_bidder[name_of_bidder] = bid_of_bidder

    user_input = input("Are there any bidder? 'yes' or 'no'.""\n").lower()

    if user_input == "no":
        in_progress = False
        
    else:
        print("\n" * 100)

# --- CALLING THE FUNCTION ---
# This runs after the loop is completely finished
    
find_highest_bidder(data_of_bidder)
