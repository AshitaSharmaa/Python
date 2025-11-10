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

resources = {
    "water": 300,
    "milk": 350,
    "coffee": 100,
    "money": 0,
}
def sufficiency_of_resources(choice):
    for item in choice:
        if choice[item] > resources[item]:
            print(f"Sorry, you don't have enough {item}")
            return False
    else:
        return True

def deduction_in_resources(choice, choice_coff):
    for item in choice:
        resources[item] -= choice[item]
    resources["money"] += MENU[choice_coff]["cost"]


# TODO: 1. Prompt user by asking “ What would you like?
should_continue = True
while should_continue:
    choice_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice_coffee == "off":
        should_continue = False

    # TODO: 3. print report
    elif choice_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    # TODO: 4. Check resources sufficient?
    else:
        resources_are_sufficient = sufficiency_of_resources(MENU[choice_coffee]["ingredients"])

        # TODO: 5. Process coins.
        if resources_are_sufficient:
            print("Please insert Coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

        # TODO: 6. Check transaction successful? Check that the user has inserted enough money to purchase the drink they selected.
            if total_money < MENU[choice_coffee]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif total_money > MENU[choice_coffee]["cost"]:
                change = round(total_money - MENU[choice_coffee]["cost"], 2)
                print(f"Here is ${change} in change. \nHere is your {choice_coffee} ☕️. Enjoy!")
                deduction_in_resources(MENU[choice_coffee]["ingredients"], choice_coffee)
            else:
                print(f"Here is your {choice_coffee} ☕️. Enjoy!")
                deduction_in_resources(MENU[choice_coffee]["ingredients"], choice_coffee)

# TODO: 7. Make Coffee. If the transaction is successful and there are enough resources to make the drink the user selected
