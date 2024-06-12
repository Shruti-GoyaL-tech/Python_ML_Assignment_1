num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(f"{num1} {op} {num2} = {num1 + num2}")

elif op == '-':
    print(f"{num1} {op} {num2} = {num1 - num2}")

elif op == '*':
    print(f"{num1} {op} {num2} = {num1 * num2}")

elif op == '/':
    print(f"{num1} {op} {num2} = {num1 / num2}")

else:
    print("Enter a valid simple calculator operator")
