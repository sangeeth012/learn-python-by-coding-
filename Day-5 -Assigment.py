import random

# Lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

user_letter = int(input("Enter number of character required in password"))
user_number = int(input("Enter number of integer present in your password"))
user_symbol = int(input("enter number of symbool present in your password"))
password =""
for i in range (user_letter):
    password += random.choice(letters)
for i in range (user_number):
    password += random.choice(numbers)
for i in range (user_symbol):
    password += random.choice(symbols)
length =len(password)
print(length)

_password = list(password)
random.shuffle(_password)
final_password = "".join(_password)
print(final_password)

