def main():
    print(value(input("Enter a greeting.\n")))


def value(greeting):
    greeting = greeting.lower().split(" ")
    if greeting[0] == "hello":
        return 100
    elif greeting[0].startswith("h"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
