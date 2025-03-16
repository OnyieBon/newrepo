num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

num1 = int(num1)
num2 = int(num2)

if operation not in ('+', '-', '*', '/'):
    print("Invalid operation. Please choose one of +, -, *, /")
    exit()

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
print(f"{num1} {operation} {num2} = {result}")