def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def divide(number1, number2):
    return number1 / number2
def multiply(number1, number2):
    return number1 * number2
print("Welcome to 4 operation caluclator")
while True:
    try:
        number1 = float(input("Enter your first number: "))
        operation = input("Enter your operation(+, -, /, *): ")
        number2 = float(input("Enter your second number: "))
        if operation == "/":
            final = divide(number1, number2)
        elif operation == "*":
            final = multiply(number1, number2)
        elif operation == "+":
            final = add(number1, number2)
        elif operation == "-":
            final = subtract(number1, number2)
        else:
            print("INVALID OPERATION")
            continue
    except ZeroDivisionError:
        print("CANNOT DIVIDE BY ZERO")
        continue
    except ValueError:
        print("Only type NUMBERS when asked please")
        continue
    else:
        break
print(f"{number1} {operation} {number2} is {final}")