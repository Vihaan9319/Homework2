import random
import math
print("========WELCOME TO THE RANDOM FUN CALCULATOR========")
lucky = random.randint(1, 10)
print(f"Your lucky number is {lucky}")
activities = ["play a game", "read a story", "draw something", "chill"]
acitivity = random.choice(activities)
print(f"Your activity is {acitivity}")
secret = random.randint(1, 5)
while True:
    try:
        guess = int(input("Guess the secret number from 1 to 5!: "))
        if guess == secret:
            print("CORRECT!")
            break
        else:
            print("Incorrect, try again")
    except ValueError:
        print("That is not a number, try again")
        continue
while True:
    try:
        decimal = float(input("Enter a decimal number: "))
    except ValueError:
        print("That is not a decimal number")
        continue
    else:
        print(f"The ceiling value of {decimal}: {math.ceil(decimal)}")
        print(f"The floor value of {decimal}: {math.floor(decimal)}")
        break
x = 5
y = -100000000000
print(f"Copysign results: {math.copysign(x, y)}")
negative = int(input("Enter a negative number: "))
print(f"Absolute value of {negative}: {math.fabs(negative)}")
while True:
    try:
        num1, num2 = input("Enter 2 numbers seperated by commas for GCD: ").split(",")
        num1 = int(num1)
        num2 = int(num2) 
    except ValueError:
        print("Enter 2 numbers seperated by commas please")
        continue
    else:
        print(f"GCD is {math.gcd(num1, num2)}")
        break
print("=========SUMMARY=========")
print(f"Lucky number: {lucky}")
print(f"Activity: {acitivity}")
print(f"Secret number: {secret}")
print("=========================")