from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    answer = input("What would you like to have ? cappuccino/ latte/ espresso:? ")
 
    if answer == "report":
        coffee_maker.report()
        money_machine.report()

    elif answer == "cappuccino" or "latte" or "espresso":       
        drink = menu.find_drink(answer)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    elif answer == "off":
        break
