print("ASCII Value Checker")
print("=" * 40)

character = input("Enter a single character: ")

if type(character) is str and len(character) == 1:
    ascii_value = ord(character)

    print(f"\nCharacter: '{character}'")
    print(f"ASCII Value: {ascii_value}")

    if ascii_value >= 65 and ascii_value <= 90:
        print("UpperCase Letter")
    elif ascii_value >= 97 and ascii_value <= 122:
        print("LowerCase Letter")
    elif ascii_value >= 48 and ascii_value <= 57:
        print("Digit")
    elif ascii_value >= 32:
        print("Space")
    else:
        print("Special Character")
else:
    print("Error: Please enter exactly ONE character!")