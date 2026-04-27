vowels = ["a", "e", "i", "o", "u"]


def main():
    user_input = input("Say something and i'll shorten it for you: ")
    output = ""
    for word in user_input.split(" "):
        output += " " + shorten(word)
    print(output)


def shorten(word):
    shortened_word = ""
    for character in word:
        if character.lower() not in vowels:
            shortened_word += character
    return shortened_word


if __name__ == "__main__":
    main()
