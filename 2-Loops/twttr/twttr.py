user_input = input("Say something and i'll shorten it for you: ")
vowels = ["a", "e", "i", "o", "u"]
output = ""

for character in user_input:
    has_vowel = False

    for vowel in vowels:
        if character.lower() == vowel:
            has_vowel = True
            break

    if has_vowel == False:
        output += character

print(output)
