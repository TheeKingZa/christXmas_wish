#!/usr/bin/python3
# Filename: holiday_wish.py
# Author: Pule Mathikha
# eMail: proceedingmc@gmail.com
# Description: A festive holiday wish program in Python
# Date: 2023-12-14

import sys
import random
from tree import tree  # {tree art} import statement
from theme import center_text_with_border, centerText, centerText_Bottom_border
from userInfo import get_user_info, load_last_five_players, save_last_five_players

# ... WORDS
def choose_word():
    """Selects a random Christmas word or phrase for the puzzle."""
    words = ["JINGLE BELLS", "CHRISTMAS TREE", "SANTA CLAUS", "FROSTY THE SNOWMAN", "HOLIDAY CHEER"]
    return random.choice(words)

# ... VICTORY MESSAGE
def display_message():
    """Displays a festive holiday message."""
    tree()  # Call the tree function to print the ASCII art
    centered_message = center_text_with_border('''
Congratulations! You've unlocked a festive holiday message:
Wishing you a Merry Christmas and a Happy New Year!
May your days be filled with joy, laughter, and warmth.
Cheers to a season of love, peace, and good company!
''')
    print(centered_message)

# ... MAIN (Play)
def play_game():
    """Runs the Christmas word puzzle game."""
    user_data = get_user_info()
    
    
    while True:  # Infinite loop for restarting the game
        word_to_guess = choose_word().upper()
        guessed_word = ["_" if char.isalpha() else char for char in word_to_guess]
        attempts = 6

        welcome_text = "Welcome to the Jingle Bells. Code Spells Christmas Challenge!"
        game_prompt = f"{user_data['name']}, Can you guess the Christmas word or phrase?"

        print(center_text_with_border(welcome_text))
        print(centerText(game_prompt))
        print(centerText_Bottom_border(" ".join(guessed_word)))
        print("")  # Empty line

        while "_" in guessed_word and attempts > 0:
            try:
                prompt = input(f"{user_data['user_id']}@Enter a letter or guess the whole word: ").upper()
                
                guess = prompt
                
                if not guess:
                    print("Empty input. Please enter a valid letter or guess the whole word.")
                    attempts -= 1
                    continue

                if len(guess) == 1 and guess.isalpha():
                    if guess in word_to_guess:
                        print(centerText("Great guess!"))
                        for i in range(len(word_to_guess)):
                            if word_to_guess[i] == guess:
                                guessed_word[i] = guess
                    else:
                        attempts -= 1
                        print(centerText(f"Oops! That letter is not in the word. {attempts}"))
                        
                        
                elif len(guess) == len(word_to_guess) and guess.isalpha():
                    if guess == word_to_guess:
                        guessed_word = list(guess)
                    else:
                        print(centerText("Incorrect guess. Try again!"))
                        attempts -= 1
                else:
                    print(centerText("Invalid input. Please enter a valid letter or guess the whole word."))

                print("Life:", attempts)
                print("\n")
                print(centerText_Bottom_border(" ".join(guessed_word)))

            except KeyboardInterrupt:
                print("\nGame interrupted. Goodbye!")
                return

        if "_" not in guessed_word:
            display_message()
        else:
            print(centerText("SORRY"))
            print(centerText("GAME OVER!."))
            print(centerText_Bottom_border(f"The word was: {word_to_guess}"))
            
            # Save user data to the last five players list
        last_five_players = load_last_five_players()
        last_five_players.append(user_data)
        if len(last_five_players) > 5:
            last_five_players.pop(0)  # Keep only the last 5 players
        save_last_five_players(last_five_players)

        # Display the last five players and the festive holiday message
        display_message(last_five_players)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thanks for playing! Goodbye!")
            sys.exit()

()
if __name__ == "__main__":
    
    play_game()

