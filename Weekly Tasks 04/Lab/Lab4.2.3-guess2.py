import random

# Initialize random number
number_to_guess = random.randint(1, 100)
# print(number_to_guess)

# Initialize the user's guess to None
user_guess = 0

# Keep asking the user to guess until they get it right
while user_guess != number_to_guess:
    # Get user input
    user_input = input("Guess the number (between 1 and 100): ")
    user_guess = int(user_input)

    # Check if the guess is correct
    if int(user_input) == number_to_guess:
        print("Congratulations! You've guessed the right number!")
    elif int(user_input) < number_to_guess:
        print("Too low, try again!")
    elif int(user_input) > number_to_guess:
        print("Too high, try again!")
