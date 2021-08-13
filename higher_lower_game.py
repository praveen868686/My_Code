from game_data import data

import random

from art import logo3, vs

import os



def pick_random_data():

    random_set = random.choice(data)

    if random_set not in question_list:

        question_list.append(random_set)

    else:

        pick_random_data()



def get_data(i,j):

    compare_a = question_list[i]['name'] + ", a " + question_list[i]['description'] + ", from " + question_list[i]['country']

    follower_a = question_list[i]['follower_count']

    print(logo3)

    print(f'Compare A: {compare_a}.')

    compare_b = question_list[j]['name'] + ", a " + question_list[j]['description'] + ", from " + question_list[j]['country']

    follower_b = question_list[j]['follower_count']

    print(vs)

    print(f'Against B: {compare_b}.')

    follower_list = [follower_a, follower_b]

    print(f'{follower_list} million follower')

    return follower_list



i = 0

j = 1

score = 0

#get the values of first item and second items in new data list

question_list = []

pick_random_data()

pick_random_data()

follower_list = get_data(i,j)

user_input = input("\nWho has more followers? Type Name A or Name B: ")



right_choice = True

while right_choice:

    if user_input == 'A' and follower_list[0] > follower_list[1]:

        score +=1

        os.system('cls')

        pick_random_data()

        i = j

        j += 1

        follower_list = get_data(i,j)

        user_input = input("\nWho has more followers? Type Name A or Name B: ")

    elif user_input == 'B' and follower_list[1] > follower_list[0]:

        score +=1

        os.system('cls')

        pick_random_data()

        i = j

        j += 1

        follower_list = get_data(i,j)

        user_input = input("\nWho has more followers? Type Name A or Name B: ")

    else:

        print(f"Sorry that's wrong, Final Score: {score} ")

        right_choice = False
