from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

gen = CoffeeMaker()
available_drinks = Menu()
user_payment = MoneyMachine()

while True:
    print("Hello there ! These are the available drinks:")
    print(available_drinks.get_items())
    user_input = input("What would you like? \n")
    # object is returned in item
    item = available_drinks.find_drink(user_input)

    if user_input == "report" or user_input == "Report":
        gen.report()
        print(user_payment.report())

    elif user_input == "Nothing" or user_input == "nothing":
        print("Thank you for your time.")
        break

    elif user_input == item.name:
        if gen.is_resource_sufficient(item):
            h = user_payment.make_payment(item.cost)
            if h:
                gen.make_coffee(item)
            else:
                print("Insufficient resources. Please try again")





