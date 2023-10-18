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
    },
}

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100}


def is_resource_sufficeint(order_ingredients):
    """Returns True when order can be made, False if ingredietns are insufficeient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("Hoe many quaters? ")) * 0.25
    total += int(input("Hoe many dimes? ")) * 0.1
    total += int(input("Hoe many nickles? ")) * 0.05
    total += int(input("Hoe many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingreditens from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


def refill(refill_item, refill_amount):
    resources[refill_item] += refill_amount
    print(f"Refilling {refill_amount} to {refill_item}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso / latte / cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill":
        refill_item = input(
            "What would you like to top-up ? (water / milk / coffee ): "
        )
        refill_amount = int(input("How much would you like to refill? "))
        refill(refill_item, refill_amount)
    else:
        drink = MENU[choice]
        if is_resource_sufficeint(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
