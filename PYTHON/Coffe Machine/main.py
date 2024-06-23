import Resources

off = False
User_input = ""
remained_resources = Resources.resources


def Terminal():
    global off
    global User_input

    User_input = input("What would you loke? (espresso/latte/cappuccino): ").lower()
    if User_input == "off":
        off = True
    elif User_input == "report":
        print(f"Water : {remained_resources['water']}ml")
        print(f"Milk : {remained_resources['milk']}ml")
        print(f"Coffee : {remained_resources['coffee']}g")
        print(f"Money : ${remained_resources['water']}")

def drink_select(drink_name):
    selected_drink = input(Resources.MENU(drink_name))

    

while not off:
    Terminal()
    print(User_input)
    print(remained_resources)
    remained_resources['water'] -= 100

print(remained_resources)    