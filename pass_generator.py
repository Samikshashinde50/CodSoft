import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    characters = ""

    # Add character sets based on user choice
    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    # Validation
    if characters == "":
        return "Error: Please select at least one character type."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


print("===== Advanced Password Generator =====")

# User input
length = int(input("Enter password length: "))

print("\nSelect character types to include:")

upper = input("Include Uppercase Letters? (y/n): ").lower() == 'y'
lower = input("Include Lowercase Letters? (y/n): ").lower() == 'y'
digits = input("Include Numbers? (y/n): ").lower() == 'y'
symbols = input("Include Special Characters? (y/n): ").lower() == 'y'

# Generate password
password = generate_password(length, upper, lower, digits, symbols)

# Display result
print("\nGenerated Password:", password)