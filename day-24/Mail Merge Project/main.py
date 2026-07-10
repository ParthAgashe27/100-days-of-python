# Count the lines
with open("./Input/Names/invited_names.txt", "r") as f:
    total_lines = sum(1 for line in f)

# Read the starting letter
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()
    
# Read the names and process them
with open("./Input/Names/invited_names.txt", "r") as invited:
    # Changed variable name to 'names_list' so it doesn't get overwritten
    names_list = invited.readlines() 
    
    # Use range() to loop through the numbers 0 up to total_lines
    for i in range(total_lines): 
        
        # 'i' acts as your line counter automatically (0, 1, 2...)
        clean_name = names_list[i].strip()
        
        # Replace the placeholder
        new_letter = content.replace("[name]", clean_name)
        
        # Save the new letter to the ReadyToSend folder
        output_path = f"./Output/ReadyToSend/letter_for_{clean_name}.txt"
        with open(output_path, "w") as final_file:
            final_file.write(new_letter)
            
        print(f"Created: {output_path}")