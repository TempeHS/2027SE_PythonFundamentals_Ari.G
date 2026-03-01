menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
order = []
cost = 0.0

while True:
    try:
        user_input = input("What would you like to order?\n")
        if user_input in menu:
            order.append(user_input)
            cost += menu[user_input]
            print("Total: $" + str(cost))
    except EOFError:
        print(order)
        print("That will be $" + str(cost))
        break
