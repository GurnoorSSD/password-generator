import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_specials=True):
    # Start with lowercase letters
    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not characters:
        return "You must select at least one character type."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# === CLI-like Input ===
try:
    length = int(input("Password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'

    pwd = generate_password(length, use_uppercase, use_digits, use_specials)
    print(f"\nGenerated password:\n{pwd}")

except ValueError:
    print("Please enter a valid number for length.")


input()

