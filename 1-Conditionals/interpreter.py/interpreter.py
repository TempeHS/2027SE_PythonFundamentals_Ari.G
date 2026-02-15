userinput = input("Input your equation: ").split()

x = float(userinput[0])
z = float(userinput[2])

match userinput[1]:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
    case _:
        print("Please include a correct mathematical operator")
