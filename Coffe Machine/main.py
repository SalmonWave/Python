import Resources

off = False

def Terminal():
    User_input = input("What would you loke? (espresso/latte/cappuccino): ").lower()
    if User_input == "off":
        off = True
    if User_input == "report":
        print(Resources.resources)



while not off:
    Terminal()


    