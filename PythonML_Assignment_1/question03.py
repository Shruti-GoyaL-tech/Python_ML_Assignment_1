num1 = int(input("Enter a number to find factorial of: "))
i = 1
factorial = 1
while i <= num1:
    factorial = factorial * i
    i += 1
print(f"Factorial of {num1} is {factorial}")
