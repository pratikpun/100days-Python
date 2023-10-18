# import another_module
# from turtle import Turtle, Screen

# tom = Turtle()
# print(tom)
# tom.shape("turtle")

# tom.color("coral")
# tom.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# from
# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_ordering = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machines = MoneyMachine()

while is_ordering:
    # print(menu.get_items())
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        is_ordering = False
    elif choice == "report":
        coffee_maker.report()
        money_machines.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machines.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
