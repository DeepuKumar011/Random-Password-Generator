import random
import string

# Basic password generator
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "Error: No character set selected!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("=== Basic Random Password Generator ===")

# Taking user input
length = int(input("Enter password length: "))

print("\nSelect password character types:")
letters = input("Include letters? (y/n): ").lower() == "y"
numbers = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate password
result = generate_password(length, letters, numbers, symbols)

print("\nGenerated Password:")
print(result)
