str1 = input("Enter a list: ")
list1 = str1.split()

element = input("Enter element of which frequency need to be found: ")

print(f"Frequency of {element} is {list1.count(element)}")
