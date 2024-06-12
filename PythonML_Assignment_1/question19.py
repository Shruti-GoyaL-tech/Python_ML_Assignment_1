str1 = str(input('Enter a string: '))
list1 = []

for char in str1:
    if ((char >= 'a') & (char <= 'z')) | ((char >= 'A') & (char <= 'Z')) | ((char >= '0') & (char <= '9')) | (char == ' '):
        list1.append(char)

str2 = ''.join(list1)

print(str2)
