def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() == False:
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    number_check = False
    for character in s:
        if character.isnumeric():
            if number_check == False and character == "0":
                return False
            else:
                number_check = True
        else:
            if number_check == True:
                return False

    if s.isalnum == False:
        return False
    return True


if __name__ == "__main__":
    main()
