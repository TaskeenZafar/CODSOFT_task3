import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Pypassword Generator!")
letters_you_choose = int(input("How many letters would you choose in your password? \n"))
numbers_you_choose = int(input("How many numbers would you choose? \n"))
symbols_you_choose = int(input("How many symbols would you choose? \n"))

password = ""
for char in range(1, letters_you_choose + 1):
    password += random.choice(letters)
for char in range(1, numbers_you_choose + 1):
    password += random.choice(numbers)
for char in range(1, symbols_you_choose + 1):
    password += random.choice(symbols)

print(password)