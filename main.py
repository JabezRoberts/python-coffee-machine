MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

pennies = 0
nickel = 0
dimes = 0
quarters = 0

total_money = 0

# TODO 1 - check resources to decide if user can do what they want
def check_resources(resources, user_choice):
    if resources["water"] < MENU["user_choice"]["water"]:




# TODO 2 - Ask the user what they would like to do, check their input, and decide what to do next
def user_choice():
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] >= resources["water"]:
            insert_coins()
        else:
            print("Sorry there is not enough water")
    elif choice == "latte"
        if MENU["latte"]["ingredients"]["water"] >= resources["water"]:
            insert_coins()
        else:
            print("Sorry there is not enough water")
    elif choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] >= resources["water"]:
            insert_coins()
        else:
            print("Sorry there is not enough water")
    elif choice == "report":
        return report(resources, total)
    elif choice == "off":
        print("The system is shutting down. Goodbye.")
        return
    else:
        print("You made an incorrect entry. Please try again")


# TODO 3 - create the function to output the report to the user when requested
def report(resources, total):
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]
    current_total = total
    return f"Water: {current_water}ml \nMilk: {current_milk}ml, \nCoffee:{current_coffee}g \nMoney: ${current_total}"

def insert_coins():
    # total_money = 0
    print("Please enter the amount of each coin you have for your payment")
    pennies_inserted = float(input("Pennies: "))
    nickels_inserted = float(input("Nickels: "))
    dimes_inserted = float(input("Dimes: "))
    quarters_inserted = float(input("Quarters: "))

    total_from_pennies = pennies_inserted * 0.01
    total_from_nickels = nickels_inserted * 0.05
    total_from_dimes = dimes_inserted * 0.1
    total_from_quarters = quarters_inserted * 0.25

    total_payment = total_from_pennies + total_from_nickels + total_from_dimes + total_from_quarters

    if total_payment == MENU["user_choice"]["cost"]:
        total_money += MENU["user_choice"]["cost"]
    elif total_payment > MENU["user_choice"]["cost"]:
        user_money = total_payment - MENU["user_choice"]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")