############## GUESS GAME #####################





logo2 = '''



#####

#     # #    # ######  ####   ####     ##### #    # ######    #    # #    # #    # #####  ###### #####

#       #    # #      #      #           #   #    # #         ##   # #    # ##  ## #    # #      #    #

#  #### #    # #####   ####   ####       #   ###### #####     # #  # #    # # ## # #####  #####  #    #

#     # #    # #           #      #      #   #    # #         #  # # #    # #    # #    # #      #####

#     # #    # #      #    # #    #      #   #    # #         #   ## #    # #    # #    # #      #   #

#####   ####  ######  ####   ####       #   #    # ######    #    #  ####  #    # #####  ###### #    #

'''



print(logo2)



import random



print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

my_number = random.randint(1, 100)

print(my_number)





def guess():

    user_guess = int(input("Guess a number: "))

    return user_guess



def compare(user_guess, my_number):

    if user_guess > my_number:

        print("\nToo High\nGuess Again\n")

        return False

    elif user_guess < my_number:

        print("\nToo Low\nGuess Again\n")

        return False

    else:

        print(f'Matches\nYou got it, the answer was {user_guess}!')

        return True



def run_game(total_attempt):

    guess_value = False

    while not guess_value:

        print(f'you have {total_attempt} attempts remaining to guess the number')

        total_attempt -= 1

        if total_attempt < 0:

            print("You have lost in the guess game")

            guess_value = True

        else:



            guess_value = compare(guess(), my_number)



difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")



if difficulty_type == 'easy':

    total_attempt = 10

    run_game(total_attempt)

elif difficulty_type == 'hard':

    total_attempt = 5

    run_game(total_attempt)

else:

    print("You'have entered wrong input as a difficulty level")
