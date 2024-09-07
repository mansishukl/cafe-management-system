# menu of restaurent
menu = {
    'Pizza': 40,
    'Burger': 60,
    'Tiramisu': 100,
    'Iced Tea': 70,
    'Coffee': 80,
}

print(menu)

# Greet
print("Welcome to Python Restaurant")
print("Pizza: Rs40\nBurger: Rs60\nTiramisu: Rs100\nIced Tea: Rs70\nCoffee: Rs80")

order_total = 0;

item_1= input("Enter the name of item = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Ordered item {item_2} has been addded to your order")

    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is {order_total}")
print("Thank you for ordering,Visit again!")


