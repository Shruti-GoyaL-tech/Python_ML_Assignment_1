str1 = input("Enter a list: ")
list1 = [int(x) for x in str1.split()]

add = 0

for i in list1:
    add += i

print(f"The sum of {list1} is {add}")
