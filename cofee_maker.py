from menu import MENU
from menu import resources

machine_on = True
report = ''
profit = 0


# change = 0

def check_resource(ingredients):
    """Checks to see if there is enough resources to make the drink requested by the user"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_payment():
    """Will return the total amount paid by the user"""
    print('Please Insert the payment')
    total = int(input("Enter amount: #"))
    return total


def check_payment(coffee_payment, cost_of_drink):
    """Checks to see if the money paid by the user can produce the drink and provide them with any change they may
    have """
    if coffee_payment >= cost_of_drink:
        global profit
        profit += cost_of_drink
        change = round(coffee_payment - cost_of_drink)
        print(f"Here is your #{change} change")
        return True
    else:
        print(f"Sorry that's not enough money, Money refunded...")
        return


def make_coffee(chosen_drink, ingredient):
    """Makes the coffee and subtract the ingredient used from the available bulk resource"""
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {chosen_drink} ☕ drink")


# Prompt user by asking "What would you like?" (espresso/latte/cappuccino)
while machine_on:
    user_input = input("What would you like?\n Espresso #150\n Latte #250\n Cappuccino #300 \n:")
    if user_input.lower() == 'off':
        machine_on = False
    if user_input.lower() == 'report':
        for i, k in resources.items():
            print(f"{i}: {k}")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_input]
        if check_resource(drink["ingredients"]):
            payment = process_payment()
            if check_payment(payment, drink['cost']):
                make_coffee(user_input, drink["ingredients"])
        order = input("Would you like to order again, 'y' or 'n':")
        if order.lower() == 'n':
            machine_on = False
