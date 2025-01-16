import random 

# def higher_lower_game():
#     target_number = random.randint(1,100)
#     attempts = 0

#     print("Welcome to the higher or lower game.")
#     print("I am thinking of a number between 1 and 100. Can you guess it.")


#     while True:
#         try:
#             user_guess = int(input("Enter your guess"))
        
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         attempts += 1

#         if user_guess < target_number:
#             print("Too low! Try again.")
#         elif user_guess > target_number:
#             print("Too high! Try again")
#         else:
#             print("Congrats.  you guessed the right number")

# higher_lower_game()


def higher_lower_game():
    target_number = random.randint(1,100)
    attempts = 0

    print("Welcome to the higher lower game.")
    print("I am thinking of a number between 1  and 100. can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        if user_guess > target_number:
            print("Too high! Try again. ")
        elif user_guess < target_number:
            print("Too low! Try again.")
        
        else:
            print("Congrats. you guessed the right number.")


higher_lower_game()