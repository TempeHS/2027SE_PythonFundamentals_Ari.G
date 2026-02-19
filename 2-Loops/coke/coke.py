cents = 0

while cents < 50:
    cents = cents + int(input("Insert a 25, 10 or 5 cent coin\n"))

print("Here's your coke 🥤")

if cents > 50:
    print(f"Please take your change of {cents - 50} cents")
