import random
import sys

user_number = int(input("Input a number\n"))

number = random.randint(1, user_number + 1)

while True:
    try:
        user_guess = int(
            input("I'm thinking of a number between 1 and " + str(user_number) + "\n")
        )
        if user_guess not in range(1, 101):
            print("Please enter a number between 1 and " + user_number + "\n")
        else:
            if int(user_guess) == number:
                print("Just right!")
                sys.exit()
            elif int(user_guess) < number:
                print("Too small!")
            elif int(user_guess) > number:
                print("Too Large!")
    except ValueError:
        print("Input is not a number\n")
