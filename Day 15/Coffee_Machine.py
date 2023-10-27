# resources
milk = 1000
water = 5000
coffee = 500
money = 0.00

# money values
penny_val = 0.01
nickel_val = 0.05
dime_val = 0.10
quarter_val = 0.25

# cost of drinks
espresso_cost = 2.75
latte_cost = 4.60
cappuccino_cost = 6.25


def check_resources(user_choice):
    es_water = 50
    es_coffee = 18
    la_water = 200
    la_milk = 150
    la_coffee = 24
    ca_water = 250
    ca_milk = 100
    ca_coffee = 24

    if user_choice == "espresso" or user_choice == "Espresso":
        if water > es_water and coffee > es_coffee:
            return 'espresso'
        else:
            return 0

    elif user_choice == "latte" or user_choice == "Latte":
        if water > la_water and coffee > la_coffee and milk > la_milk:
            return 'latte'
        else:
            return 0
    elif user_choice == "cappuccino" or user_choice == "cappuccino":
        if water > ca_water and coffee > ca_coffee and milk > ca_milk:
            return 'cappuccino'
        else:
            return 0


def check_money(q_amount, d_amount, n_amount, p_amount):
    change = 0
    if user_input == "espresso":
        user_money = (q_amount * quarter_val) + (d_amount * dime_val) + (n_amount * nickel_val) + (p_amount * penny_val)
        change = user_money - espresso_cost
        if change > 0:
            return change
        elif change < 0:
            return 'Not enough money.'
    elif user_input == "latte":
        user_money = (q_amount * quarter_val) + (d_amount * dime_val) + (n_amount * nickel_val) + (p_amount * penny_val)
        change = user_money - latte_cost
        if change > 0:
            return change
        elif change < 0:
            return 'Not enough money.'
    elif user_input == "cappuccino":
        user_money = (q_amount * quarter_val) + (d_amount * dime_val) + (n_amount * nickel_val) + (p_amount * penny_val)
        change = user_money - cappuccino_cost
        if change > 0:
            return change
        elif change < 0:
            return 'Not enough money.'


def update_resources(user_drink, money_update):
    global water
    global milk
    global coffee
    global money
    if user_drink == "espresso":
        water -= 50
        coffee -= 18
        money += 2.75
    elif user_drink == "latte":
        water -= 200
        milk -= 150
        coffee -= 24
        money += 4.60
    elif user_drink == "cappuccino":
        water -= 250
        milk -= 100
        coffee -= 24
        money += 6.25


def report():
    print(f"Current water: {water} mL")
    print(f"Current milk: {milk} mL")
    print(f"Current coffee: {coffee} gm")
    print(f"Current money: $ {money} ")


while True:
    user_input = input("What would you like? \n")

    if user_input == "report" or user_input == "Report":

        report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        resources = check_resources(user_input)

        if resources == user_input:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            money_enough = check_money(quarters, dimes, nickles, pennies)

            if money_enough == "Not enough money.":
                print("Sorry not enough money, your amount has been refunded.\nPlease try again.")
            elif money_enough > 0:

                print(f"Here is your {user_input}.")
                print(f"And here is the change: {money_enough}")

                update_resources(user_input, money_enough)

        elif resources == 0:
            print(f"Sorry, not enough resources for {user_input}.")

    elif user_input == "nothing" or user_input == "Nothing":
        print("Thank you ! Have a great day.")
        break
