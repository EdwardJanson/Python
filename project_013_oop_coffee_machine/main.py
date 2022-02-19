from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    drink_selected = input(f"What would you like? ({Menu.get_items(menu)}): ")
    if drink_selected == "off":
        machine_on = False
    elif drink_selected == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_detail = menu.find_drink(drink_selected)
        sufficient_resources = coffee_maker.is_resource_sufficient(drink_detail)
        if sufficient_resources:
            payment_sufficient = money_machine.make_payment(drink_detail.cost)
            if payment_sufficient:
                coffee_maker.make_coffee(drink_detail)
                coffee_maker.report()
