MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(drink_name, choice_resources):
    for item in choice_resources:
        resources[item] -= choice_resources[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def enough_resources(choice_resources):
    for item in resources:
        if choice_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def payment():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def enough_money(money_received, coffee_cost):
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


running = True
while running:
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == 'off':
        running = False
    elif choice == 'resources':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink['ingredients']):
            pay = payment()
            if enough_money(pay, drink['cost']):
                make_coffee(choice, drink['ingredients'])
