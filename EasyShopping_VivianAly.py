import sys
from csv import reader
with open('itemsList_VivianAly.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_items = list(csv_reader)

cart = []

def mainMenu():
    while True:
        print('''

            Hello, Welcome to Easy Shopping!
            Please select a number for the action that you would like to do:

            1. View item list
            2. Add item to cart
            3. View cart
            4. Remove item from cart
            5. Check if item is in cart
            6. How many items in cart
            7. Clear cart
            8. Exit
            ''')
        print()
        selection = input("Make your selection: ")

        if selection == "1":
            print_items()
        elif selection == "2":
            add_item()
        elif selection == "3":
            print_cart()
        elif selection == "4":
            remove_item()
        elif selection == "5":
            in_cart()
        elif selection == "6":
            count()
        elif selection == "7":
            clear_cart()
        else:
            sys_exit()
            sys.exit()


def print_items():
    print()
    print("    price      Product Name")
    print()
    for i in range(1, len(list_of_items)):
        print(
            f"      ${float(list_of_items[i][2])}                {list_of_items[i][1]}")


def add_item():
    print()
    name = input("Enter item name: ").lower()
    num = int(input("How many? "))
    for i in range(len(list_of_items)):
        if list_of_items[i][1] == name:
            for j in range(num):
                cart.append(list_of_items[i])
            print(name + " has been added to cart.")


def print_cart():
    print()
    print("    price      Product Name")
    print()
    total_price = 0.0
    for i in range(len(cart)):
        total_price += float(cart[i][2])
        print(
            f"      ${float(cart[i][2])}                {cart[i][1]}")
    print("\n Total price is $",total_price)


def remove_item():
    print()
    name = input("Enter item name: ").lower()
    for item in cart:
        if item[1] == name:
            cart.remove(item)
            print(name + " has been removed from cart.")


def in_cart():
    print()
    name = input("Enter item name: ").lower()
    flag = False
    for item in cart:
        if item[1] == name:
            flag = True
    if flag == True:
        print("Item already exist")
    else:
        print("Item does not exist")


def count():
    print()
    print(f"       ****    There are {len(cart)} items in cart     ****")


def clear_cart():
    cart.clear()


def sys_exit():
    print()
    print("    price      Product Name")
    print()
    total_price = 0.0
    for i in range(len(cart)):
        total_price += float(cart[i][2])
        print(
            f"      ${float(cart[i][2])}                {cart[i][1]}")
    print("Your total price is $",total_price,", have a nice day, goodbye!")
   

mainMenu()
