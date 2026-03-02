items = {}

while True:
    try:
        user_input = input("What would you like to buy?\n").upper()
        if user_input in items:
            items[user_input] += 1
        else:
            items[user_input] = 1
    except EOFError:
        for item in sorted(items):
            print(items[item], item)
        break
