from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
money_machine = MoneyMachine()
menuItem = MenuItem
end_coffee = False

while not end_coffee:
    choose = input(f"What would you like? ({menu.get_items()}): ")
    if choose == "report":
        coffeeMaker.report()
        money_machine.report()
    elif choose == "off":
        end_coffee = True
    else:
        drink = menu.find_drink(choose)
        if drink is not None:
            if coffeeMaker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)
