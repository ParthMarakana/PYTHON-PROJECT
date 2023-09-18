resource = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

Menu = {
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 2.5
    },

    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 2.00
    },
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 1.5
    }
}

sufficient = True


def check_sufficient(totals, res_type, coffee_type):
    global sufficient

    if res_type == "money" and totals < Menu[coffee_type][res_type]:
        print(f"there is not enough {res_type}")
        print(f"Here is your money {totals}")
        print( Menu[coffee_type][res_type])
        sufficient = False

    elif res_type != "money" and resource[res_type] < Menu[coffee_type][res_type]:
        print(f"there is not enough {res_type}")
        print(f"Here is your money {totals}")
        sufficient = False


def take_coins():

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many Dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


while True:
    answer = input("what would you like to have?? (espresso/ latte/ cappuccino )")

    if answer == "report":
        print(f" water : {resource['water']}ml \n Milk : {resource['milk']}ml \n Coffee : {resource['coffee']}g \n "
              f"Money : {resource['money']}$")

    elif answer == ("latte" or "espresso" or "cappuccino"):
        print("Please insert coins.")

        total = take_coins()

        for key in Menu[answer]:
            check_sufficient(total, key, answer)

        if sufficient:

            resource["milk"] -= Menu[answer]["milk"]
            resource["water"] -= Menu[answer]["water"]
            resource["coffee"] -= Menu[answer]["coffee"]
            resource["money"] += Menu[answer]["money"]
            total -= Menu[answer]["money"]

            print(f" Take your {answer}")
            print(f" Here is your change {total}")
    elif answer == "off":
        print("Turning off")
        break
