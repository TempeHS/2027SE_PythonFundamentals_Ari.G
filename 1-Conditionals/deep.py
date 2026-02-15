useranswer = input("What is the meaning of life? ").lower()

match useranswer:
    case "42" | "forty-two" | "forty two":
        print("Correct!")
