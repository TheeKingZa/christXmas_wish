# Filename: userInfo.py
# Author: Pule Mathikha
# eMail: proceedingmc@gmail.com
# Description: Helper functions for user information
# Date: 2023-12-14

import hashlib
import os
import sys
from theme import centerText

def generate_user_id(user_name):
    """Generates a unique user ID based on the user's name."""
    user_name_bytes = user_name.encode('utf-8')
    return hashlib.md5(user_name_bytes).hexdigest()[:4]

def get_user_info():
    """Gets user information from the user."""
    try:
        user_name = input("What's your name? ")
    except KeyboardInterrupt:
        print(centerText("\n... GameBy_Pule_Mathikha ..."))
        print("\t\t\tGoodBye and Happy Holidays !!!")
        sys.exit()

    if not user_name:
        print("Name cannot be empty. Please enter a valid name.")
        return get_user_info()

    user_id = generate_user_id(user_name)
    print(f"Hello, {user_name}! Your unique user ID is: {user_id}")

    return {"name": user_name, "user_id": user_id}

def load_last_five_players():
    """Loads the information of the last five players from a file."""
    file_path = "last_five_players.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            players = eval(file.read())
            return players
    return []

def save_last_five_players(players):
    """Saves the information of the last five players to a file."""
    file_path = "last_five_players.txt"
    with open(file_path, "w") as file:
        file.write(repr(players))
