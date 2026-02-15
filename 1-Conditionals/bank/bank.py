userinput = input("Enter a greeting: ").lower().strip()

if userinput.startswith("hello"):
    print("You get $0")
elif userinput.startswith("h"):
    print("You get $20")
else:
    print("You get $100")
