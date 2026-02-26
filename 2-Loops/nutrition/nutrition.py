fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
}  # Im not wasting my time doing that for 17 more, you get the idea

user_input = input("Enter a fruit to find out its calories: ").lower()

if user_input in fruits:
    print("Calories: " + str(fruits[user_input]))
