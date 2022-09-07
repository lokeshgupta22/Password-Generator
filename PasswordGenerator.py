import string
import random

letters = list(string.ascii_letters)
# print(letters)

numbers = list(string.digits)
# print(numbers)

#symbols = list(string.punctuation)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print(symbols)

print("Welcome to PyPassword Generator")
numL = int(input("How many letters do you want to generate? \n"))
numD = int(input("How many digits do you want in the password? \n"))
numS = int(input("How many symbols do you want in the password? \n"))

pw = []  # using List
for i in range(0, (numL)):
    pw.append(random.choice(letters))
for i in range(0, (numD)):
    pw += random.choice(numbers)
for i in range(0, (numS)):
    pw += random.choice(symbols)
print(pw)
random.shuffle(pw)
print(pw)
# print(f"{''.join(pw)}") #One line method for below code
password = ""
for i in pw:
    password += i
print(f"Your Password is: {password}")
