from data import MENU, resources


def get_user_coins():
    user_quarters = int(input("Please insert the coins\nHow many quarters? "))
    user_dimes = int(input("How many dimes? "))
    user_nickels = int(input("How many nickels? "))
    user_pennies = int(input("How many pennies? "))
    user_coin_value = (user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickels * 0.05) + (user_pennies * 0.01)
    return round(user_coin_value, 2)


def get_beverage_cost(beverage):
    """returns the cost of beverage"""
    beverage_cost = MENU[beverage]['cost']
    return beverage_cost


def get_beverage_ingredients(beverage):
    """returns the ingredients of beverage"""
    beverage_ingredients = MENU[beverage]['ingredients']
    return beverage_ingredients


def compare_resources(bev_resources, current_res):
    """function to check if there are sufficient resources"""
    if current_res['water'] > bev_resources['water']:
        if current_res['coffee'] > bev_resources['coffee']:
            # no milk scenario handled for espresso
            if 'milk' in bev_resources:
                if current_res['milk'] > bev_resources['milk']:
                    return True
                else:
                    return "not enough milk"
            else:
                return True
        else:
            return "not enough coffee"
    else:
        return "not enough water"


def current_resource():
    """to update the resources once the beverage is taken"""
    resources['water'] = resources['water'] - beverage_resources['water']
    resources['coffee'] = resources['coffee'] - beverage_resources['coffee']
    # no milk scenario handled for espresso
    if 'milk' in beverage_resources:
        resources['milk'] = resources['milk'] - beverage_resources['milk']


money = 0
should_continue = True
while should_continue:
    user_choice = input("Select your beverage: ").lower()
    if user_choice == 'report':
        for i in resources:
            if i == 'water' or i == 'milk':
                print(f"{i}: {resources[i]}ml")
            else:
                print(f"{i}: {resources[i]}g")
        print(f"Money: ${money}")
    elif user_choice == 'off':
        should_continue = False
    elif user_choice in ['espresso', 'latte', 'cappuccino']:
        beverage_resources = get_beverage_ingredients(user_choice)
        sufficient_resource = compare_resources(beverage_resources, resources)
        if sufficient_resource == True:
            user_coin_amount = get_user_coins()
            beverage_amount = get_beverage_cost(user_choice)
            money += beverage_amount
            if user_coin_amount > beverage_amount:
                change = round((user_coin_amount - beverage_amount), 2)
                print(f"Here is your ${change} dollars in change\nEnjoy your {user_choice} ☕☕☕☕☕☕")
                current_resource()
            else:
                print("Sorry that's not enough money. Money refunded.")
                should_continue = False
        else:
            print(f"Sorry there is {sufficient_resource}")
            should_continue = False
    else:
        print("you have entered invalid beverage choice")
