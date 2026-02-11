def convert(userstring):
    return userstring.replace(":)", "🙂").replace(":(", "🙁")


def main():
    userinput = input("type a :) or a ): and watch what happens")
    print(convert(userinput))


main()
