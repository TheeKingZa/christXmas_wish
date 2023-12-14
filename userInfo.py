# ... Modules
import random
import json

# Initialize a set to keep track of used user_ids
used_user_ids = set()

# Function to generate a consistent user ID based on the user name
# Function to generate a consistent user ID based on the user name
def generate_user_id(user_name):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Load existing user data from data_file.json
    existing_users = {}
    try:
        with open("data_file.json", "r") as json_file:
            existing_users = json.load(json_file)
    except FileNotFoundError:
        pass  # If the file doesn't exist, just continue

    # If the user already exists, return their existing user_id
    if user_name in existing_users:
        return existing_users[user_name]["user_id"]

    # Generate a new user ID if the user doesn't exist
    user_id = ''.join(random.choice(characters) for _ in range(4))  # Keep it 4 characters

    # Update the existing user data
    existing_users[user_name] = {"user_id": user_id}

    # Save the updated user data to data_file.json
    with open("data_file.json", "w") as json_file:
        json.dump(existing_users, json_file)

    return user_id

# user information
def get_user_info():
    # Ensure the user_name is unique and 4 characters
    while True:
        user_name = input("What's your name? ").capitalize()  # Ensure the first letter is capital
        if len(user_name) == 4 and user_name.isalpha():
            break
        else:
            print("Invalid name. Please enter a unique 4-character name.")

    user_id = generate_user_id(user_name)
    
    user_data = {
        "name": user_name,
        "user_id": user_id
    }

    with open("data_file.json", "w") as json_file:
        json.dump(user_data, json_file)

    return user_data 
# Function to load the last five players from the JSON file
def load_last_five_players():
    try:
        with open("last_five_players.json", "r") as json_file:
            last_five_players = json.load(json_file)
    except FileNotFoundError:
        last_five_players = []
    return last_five_players

# Function to save the last five players to the JSON file
def save_last_five_players(last_five_players):
    with open("last_five_players.json", "w") as json_file:
        json.dump(last_five_players, json_file)

