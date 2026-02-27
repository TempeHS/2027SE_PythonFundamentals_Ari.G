while True:
    user_input = input("Input a fraction: ").split("/")
    try:
        tank = round(int(user_input[0]) / int(user_input[1]) * 100)
        if tank <= 0:
            print("E")
            break
        else:
            print(str(tank) + "%")
            break
    except ValueError:
        print("Please enter a valid fraction")
    except ZeroDivisionError:
        print("Please enter a valid fraction")
