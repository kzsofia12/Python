MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


def check_resources(coffee, resource):
    if MENU[coffee]["ingredients"][resource] > resources[resource]:
        return False
    return True

    # TODO: Process coins


def insert_coin():
    print("Please insert coins.")
    quart = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nick = float(input("How many nickles?: "))
    penny = float(input("How many pennies?: "))
    coins = quart * 0.25 + 0.1 * dimes + 0.05 * nick + 0.01 * penny
    return coins


def coffee(user_ask):
    if check_resources(user_ask, "water") and check_resources(user_ask, "milk") and check_resources(user_ask, "coffee"):
        coin = insert_coin()
        if MENU[user_ask]["cost"] > coin:
            print("Sorry that's not enough money. Money refund")
        else:
            resources["water"] -= MENU[user_ask]["ingredients"]["water"]
            resources["milk"] -= MENU[user_ask]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_ask]["ingredients"]["coffee"]
            global money
            money += MENU[user_ask]["cost"]
            change = round(coin - MENU[user_ask]["cost"], 2)
            print(f"Here is ${change} in change. ")
            print(f"Here is your {user_ask}. Enjoy.")
    elif not check_resources(user_ask, "water"):
        print("Sorry there is not enough water")
    elif not check_resources(user_ask, "milk"):
        print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough sugar")


turn_off = False


while not turn_off:
    user_ask = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: Turn off coffee machine
    if user_ask.lower() == "off":
        turn_off = True
    # TODO: Print report
    elif user_ask.lower() == "report":
        report()
    # TODO: Check resources
    elif user_ask.lower() == "espresso" or user_ask.lower() == "latte" or user_ask.lower() == "cappuccino":
        coffee(user_ask.lower())

