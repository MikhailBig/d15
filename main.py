from data import MENU as menu
from data import resources
from data import coins
from prompt_toolkit.shortcuts.utils import clear
import re


def report():
    for n, v in resources.items():
        print(f"{n.capitalize()}: {v}")


def stop_operate():
    global end
    end = True
    return end


def make_drink(drink):
    print(f"Price for shot of {drink} is: ${menu[drink]['cost']}")
    print("*** Insert coins.")
    money_recieved = 0
    for coin, weight in coins.items():
        inserted = input(f"How many {coin}: ")
        while not re.match('[0-9]', inserted):
            inserted = input(f"How many {coin}: ")
        weight = int(inserted)*weight
        money_recieved += weight
    if money_recieved < menu[drink]['cost']:
        return print("*** Not enough money. Coins refunded.")
    elif money_recieved >= menu[drink]['cost']:
        for ingredient, value in menu[drink]['ingredients'].items():
            if resources[ingredient] - value < 0:
                return print(f"*** Not enogh {ingredient}. Coins refunded")
        for ingredient, value in menu[drink]['ingredients'].items():
            resources[ingredient] = resources[ingredient] - value
        print(f"*** Making {drink}....will take a while....")
        return print(f"Here is your {drink}. With ${round(money_recieved-menu[drink]['cost'], 2)} change.")


def check_resources():
    for ingredient, value in menu['espresso']['ingredients'].items():
        if resources[ingredient] < value:
            print(f"\n*** Not enough {ingredient}, please fill the tank ***\n")


def start():
    check_resources()
    task = input("What would you like? (espresso/latte/cappuccino): ")
    while task not in operations.keys():
        task = input("Invalid operation\nTry again: ")
    if task in menu:
        operations[task](task)
    else:
        operations[task]()


operations = {
    'report': report,
    'exit': stop_operate,
    'espresso': make_drink,
    'latte': make_drink,
    'cappuccino': make_drink,
}
end = False
clear()

while not end:
    start()
