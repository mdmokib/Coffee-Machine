from multiprocessing.connection import XmlListener
from statistics import median_low

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

def is_resource_enough(order_ingredients):
    """Returns true when order can be made and false when resources is not sufficient"""
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry, we don't have enough {items}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when transaction was successful, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(F"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough money.")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resourcesS"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}☕ coffee now.")


is_on= True
while is_on:
     choice = input("What do you like? (espresso/latte/cappuccino): ")
     if choice == "off":
         is_on = False
     elif choice == "report":
         print(f"Water: {resources['water']}")
         print(f"Milk : {resources['milk']}")
         print(f"Coffee: {resources['coffee']}")
         print(f"Money: ${profit}")
     else:
         drink = MENU[choice]
         if is_resource_enough((drink["ingredients"])):
             payment = process_coins()
             if is_transaction_successful(payment, drink["cost"]):
                 make_coffee(choice, drink["ingredients"])




