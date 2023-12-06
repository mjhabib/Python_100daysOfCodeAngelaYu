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
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "money": 0.0,
}


def off_switch():
    print("The machine is no longer available!")
    quit()


def report():
    for i in resources:
        print(f"{i} = {resources[i]}")


def check_resources(coffee_type):
    desired_coffee = MENU[coffee_type]
    desired_coffee = desired_coffee['ingredients']  # I need to compare ingredients together not the whole dict

    go_make_coffee = True
    for i in desired_coffee:
        if desired_coffee[i] > resources[i]:
            print(f"Sorry, not enough {i}")
            go_make_coffee = False
        # I couldn't put an 'else' here because I'm inside a 'for loop'
    if go_make_coffee:
        process_coins(coffee_type)


def process_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    coffee_price = MENU[coffee_type]
    if coins == coffee_price['cost']:
        print(f"Here is your '{coffee_type} ☕', enjoy :)")
        recalculate_resources(coffee_type)
    elif coins > coffee_price['cost']:
        print(f"Here is your '{coffee_type} ☕' enjoy :)")
        coins -= coffee_price['cost']
        print(f"And here is your '${coins:.2f}' remainder. ")  # print only two decimals
        recalculate_resources(coffee_type)
    else:
        print(f"Sorry, your '{coffee_type}' costs '${coffee_price['cost']}'. Here is your '${coins}' refunded.")


def recalculate_resources(coffee_type):
    spent_ingredients = MENU[coffee_type]
    spent_ingredients = spent_ingredients['ingredients']
    spent_money = MENU[coffee_type]
    spent_money = spent_money['cost']

    for i in resources:
        if i == 'money':
            resources['money'] += spent_money
        else:
            resources[i] -= spent_ingredients[i]

    # without for-loop:
    # resources['water'] -= spent_ingredients['water']
    # resources['milk'] -= spent_ingredients['milk']
    # resources['coffee'] -= spent_ingredients['coffee']
    # resources['money'] += spent_money


on_switch = True  # endless loop until user switches off the machine
while on_switch:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        off_switch()
    elif order == 'report':
        report()
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        check_resources(coffee_type=order)
    else:
        print("Your input is invalid!")

# tip: Alt + Shift and drag == multi-line editing
