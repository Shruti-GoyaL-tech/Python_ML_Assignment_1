frequency_dictionary = {}
str1 = str(input('Enter a string: '))

for char in str1:
    if char in frequency_dictionary:
        frequency_dictionary[char] += 1
    else:
        frequency_dictionary[char] = 1

print(frequency_dictionary)
