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

# Machine resources and money collected
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(drink):
    """Check if there is enough resources to make the drink"""
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def get_coins():
    """Prompt the user to get the number of coins"""
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies

def update_resources(drink):
    """Update the resource amounts after drink has been paid for"""
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    resources["profit"] += MENU[drink]["cost"]

def make_coffee():
    """Main coffee machine logic"""
    machine_on = True

    while machine_on:
        # TODO 1: Prompt the user
        selection = input("What would you like? ").lower()

        if selection == "off":
            # TODO 2: Shut down the machine
            machine_on = False

        elif selection == "report":
            # TODO 3: Print report - Display current resource levels
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")

        elif selection in ["espresso", "latte", "cappuccino"]:
            # TODO 4: Check ingredient availability
            if check_resources(selection):
                # TODO 5: Process payment
                paid = get_coins()
                # TODO 6: Validate payment amount
                if paid < MENU[selection]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    continue
                
                # Provide change and make the drink
                change = round(paid - MENU[selection]["cost"], 2)
                print(f"Here is ${change} dollars in change.")
                update_resources(selection)
                print(f"Here is your {selection} ☕️. Enjoy!")

make_coffee()
