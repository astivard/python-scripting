from menu import MENU, resources


def asking():
    requests = ["espresso", "latte", "cappuccino", "report", "off"]
    while True:
        type_of_coffee = input("What would you like?\n"
                               "espresso - $1.5\n"
                               "latte - $2.5\n"
                               "cappuccino - $3.0\n"
                               "report - if you want to check coffee machine resources\n"
                               "Type here: ").lower()
        if type_of_coffee in requests:
            break
    return type_of_coffee


def report(income):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water:  {water} ml\nMilk:   {milk} ml\nCoffee: {coffee} g\nMoney:  ${income}")


def check_resources(request):
    if resources["water"] < MENU[request]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return 1
    if request != "espresso" and resources["milk"] < MENU[request]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return 1
    if resources["coffee"] < MENU[request]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return 1
    return 0


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))  # 25 cents
    dimes = int(input("How many dimes: ")) # 10 cents
    nickles = int(input("How many nickles: ")) # 5 cents
    pennies = int(input("How many pennies: "))  # 1 cent
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return round(money, 2)


def coffee_machine():
    income = 0
    should_continue = True
    while should_continue:
        request = asking()
        if request == "report":
            report(income)
        elif request == "off":
            should_continue = False
            print("Coffee machine is off.")
        else:
            if check_resources(request) == 0:
                coins = insert_coins()
                if coins < MENU[request]["cost"]:
                    print(f"Amount deposited is ${coins}.")
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] -= MENU[request]["ingredients"]["water"]
                    if request != "espresso":
                        resources["milk"] -= MENU[request]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
                    income += MENU[request]["cost"]
                    change = round(coins - MENU[request]["cost"], 2)
                    print(f"Amount deposited is ${coins}.")
                    if coins > MENU[request]["cost"]:
                        print(f"Here is ${change} in change.")
                    print(f"Here is your {request} ☕. Enjoy!")
            else:
                break
        print()


if __name__ == "__main__":
    coffee_machine()
