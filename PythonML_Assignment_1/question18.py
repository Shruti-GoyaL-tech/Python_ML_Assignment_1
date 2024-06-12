str1 = str(input('Enter a string: '))
str2 = str(input('Enter a string: '))

frequency_dictionary1 = {}
frequency_dictionary2 = {}

for char in str1:
    if char in frequency_dictionary1:
        frequency_dictionary1[char] += 1
    else:
        frequency_dictionary1[char] = 1

for char in str2:
    if char in frequency_dictionary2:
        frequency_dictionary2[char] += 1
    else:
        frequency_dictionary2[char] = 1

if frequency_dictionary1 == frequency_dictionary2:
    print(f"{str1} and {str2} are anagrams of each other")

else:
    print(f"{str1} and {str2} are not anagrams of each other")
