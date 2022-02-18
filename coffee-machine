from data import MENU
from data import resources


def select_drink():
    return input("What would you like? (espresso/latte/cappuccino): ")


def sum_paid(item, price):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_change = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    if price > total_change:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif price == total_change:
        print(f"Here is your {item}. Enjoy!")
        return True
    else:
        print(f"Here is ${round(total_change - price, 2)}\nHere is your {item}. Enjoy!")
        return True


def item_resources(item, water_left, milk_left, coffee_left):
    water_used = MENU[item]["ingredients"]["water"]
    water_left -= water_used
    coffee_used = MENU[item]["ingredients"]["coffee"]
    coffee_left -= coffee_used
    if item != "espresso":
        milk_used = MENU[item]["ingredients"]["milk"]
        milk_left -= milk_used

    if water_left < 0 and milk_left < 0 and coffee_left < 0 and item != "espresso":
        print("Sorry, we ran out of water, milk and coffee.")
        return False
    elif water_left < 0 and coffee_left < 0:
        print("Sorry, we ran out of water and coffee.")
        return False
    elif water_left < 0 and milk_left < 0:
        print("Sorry, we ran out of water and milk.")
        return False
    elif milk_left < 0 and coffee_left < 0:
        print("Sorry, we ran out of water and milk.")
        return False
    elif milk_left < 0 and item != "espresso":
        print("Sorry, we ran out of milk.")
        return False
    elif coffee_left < 0:
        print("Sorry, we ran out of coffee.")
        return False
    elif water_left < 0:
        print("Sorry, we ran out of water.")
        return False
    else:
        return True


water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]

serve_drink = True

while serve_drink:
    drink_selected = select_drink()
    drink_price = MENU[drink_selected]["cost"]
    resource_check = item_resources(drink_selected, water_resource, milk_resource, coffee_resource)
    if resource_check:
        print("Please insert coins.")
        change_check = sum_paid(drink_selected, drink_price)
        if change_check:
            water_resource -= MENU[drink_selected]["ingredients"]["water"]
            coffee_resource -= MENU[drink_selected]["ingredients"]["coffee"]
            if drink_selected != "espresso":
                milk_resource -= MENU[drink_selected]["ingredients"]["milk"]
            enough_resources = False
