import random
import sys


def get_level():
    user_level = int
    while user_level not in (1, 2, 3):
        user_level = int(input("Enter a difficulty level between 1 and 3\n"))
    match user_level:
        case 1:
            return [
                int("1".rjust(int(user_level))),
                int("9".rjust(int(user_level))),
            ]
        case 2:
            return [
                int("10".rjust(int(user_level))),
                int("99".rjust(int(user_level))),
            ]
        case 3:
            return [
                int("100".rjust(int(user_level))),
                int("999".rjust(int(user_level))),
            ]


def generate_number(level):
    return random.randint(1, level)


def main():
    level = get_level()
    for _ in range(10):
        number_1 = random.randint(level[0], level[1])
        number_2 = random.randint(level[0], level[1])
        answer = str(number_1 + number_2)
        guesses = 0
        correctanswers = 0
        while guesses < 3:
            user_input = input(f"What's {number_1} + {number_2}?\n")
            if user_input == answer:
                print("Correct!")
                correctanswers += 1
                break
            else:
                guesses += 1
        print("The answer was " + answer)
    print("You got " + correctanswers + " out of 10")


main()
