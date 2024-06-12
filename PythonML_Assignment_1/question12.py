num1 = int(input("Enter a number: "))
num2 = num1
add = 0
while num2 != 0:
    add += num2 % 10
    num2 = num2 // 10

print(f"Sum of digits of {num1} is {add}")
