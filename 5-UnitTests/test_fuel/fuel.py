def main():
    print(check_fuel(input("Input a fraction: ")))


def check_fuel(input):
    input = input.split("/")
    try:
        tank = round(int(input[0]) / int(input[1]) * 100)
        if tank <= 0:
            return "E"
        else:
            return str(tank) + "%"
    except ValueError:
        return "Please enter a valid fraction"
    except ZeroDivisionError:
        return "Please enter a valid fraction"


if __name__ == "__main__":
    main()
