str1 = str(input("Enter a string: "))
substr1 = str(input("Enter a substring: "))
if substr1 in str1 :
    print(f"Substring {substr1} is present in {str1}")
else:
    print(f"Substring {substr1} is not present in {str1}")
