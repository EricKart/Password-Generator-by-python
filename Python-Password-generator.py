from lib2to3.pygram import Symbols
import numbers
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
Symbols = ['!', '#', '@', '$', '%', '&', '*', '+', '(', ')']
print("Welcome to password generator!")
no_letters = int(input("Enter the number of letters you want in your password!: "))
no_symbols = int(input("Entere the number of symbols you want in your password!: "))
no_numbers = int(input("Enter the number of numbers you want in your password!: "))


Password_list = []

for char in range (1, no_letters+1):
    Password_list.append(random.choice(letters))

for num in range(1, no_numbers+1):
    Password_list.append(random.choice(numbers))

for sym in range(1, no_symbols):
    Password_list.append(random.choice(Symbols))

random.shuffle(Password_list)


Password = " "
for char in Password_list:
    Password += char


print(f"Your most trusted password is ready: {Password}")