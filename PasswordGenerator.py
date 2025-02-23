"""
A tool that generates a random secure password based on user preferences.

Requirements:
- Ask the user for password length
- Allow the user to include uppercase, lowercase, numbers, and special characters
- Generate a random password
- Display the generated password
"""
import string
import random

def generate_password(length):
    combos = list(string.ascii_letters) + list(string.digits) + list("!@#$%^&*")
    password = "".join(random.choice(combos) for _ in range(length))
    return password

print("Generate a secure password.")
print("Enter length of password: ")
length = int(input())
password = generate_password(length)

print("\nGenerating password...")
print(password)