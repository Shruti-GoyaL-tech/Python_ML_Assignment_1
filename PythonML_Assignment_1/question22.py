str1 = input("Enter a list: ")
list1 = [int(x) for x in str1.split()]

print(f"Minimum element in {list1} is {min(list1)}")
print(f"Maximum element in {list1} is {max(list1)}")
