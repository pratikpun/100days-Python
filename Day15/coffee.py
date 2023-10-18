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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

is_machine_on = True

while is_machine_on:
    user_input = input("What would you like? (espresso / latte / cappuccino): ").lower()
    print(f"Getting your {user_input} ready . . . ")

    if user_input == "off":
        is_machine_on = False

    if user_input == "report":
        for item in resources:
            if item == "money":
                resources["money"] = "$" + str(resources[item])
            print(f"{item.title()} : {resources[item]}")

    for item in MENU:
        for resource_item in resources:
            print(f"From resources: {resources[resource_item]}")
            print(f"From Menu: {MENU[item]['ingredients'][resource_item]}")
            # water = int(resources[resource_item] - int(item[resource_item]))
            # print(water)
