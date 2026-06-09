import random
import hangman_words
import hangman_art

lives_to_guess_the_word = 6

print(hangman_art.logo) #from module - fully cosmetics

chosen_word = random.choice(hangman_words.word_list) #from module - fully cosmetics

list_chosen_word = list(chosen_word)  

# print(chosen_word)

placeholder = chosen_word
for letter in chosen_word: 
        placeholder = placeholder.replace(letter, "_")

print(placeholder)

game_over = False
correct_letters = []
#**************************MOST IMP PART OF THE CODE**************************************
while not game_over:
    print(f"****************************<{lives_to_guess_the_word}>/6 LIVES LEFT****************************")
    input_letter = input("Guess a letter: ").lower()

    if input_letter in chosen_word: #to let user know they guess it already
        print("The letter you guessed is in the word")

    display = ""

    for letter in list_chosen_word: #checks the letter guessed if == adds to display, elif check in correct_letter if yes adds in display, else prints "_" in display
        if letter == input_letter:
            display += letter
            correct_letters.append(input_letter)

        elif letter in correct_letters:
             display += letter

        else:
            display += "_"

    print("Word to guess: " + display) 


    if input_letter not in chosen_word: #checks players lives 
         lives_to_guess_the_word -= 1

         print(f"You guessed {input_letter}, that's not in the word. You lose a life.")


         if lives_to_guess_the_word == 0:
              game_over = True
              print(f"***********************YOU LOSE**********************")
              print("The word was: " + chosen_word)

         
    if "_" not in display:
         game_over = True
         print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives_to_guess_the_word]) #from module - fully cosmetics
