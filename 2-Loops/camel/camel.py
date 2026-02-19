user_input = input("Input a variable name in camel case:\n")


def main():
    print(convert(user_input))


def convert(string):
    output = ""
    for character in user_input:
        if character == character.upper():
            output = output + "_" + character
        else:
            output = output + character
    return output.lower()


main()
