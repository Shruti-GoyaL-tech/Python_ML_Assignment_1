str1 = input("Enter a string: ")

prefix = input("Enter given prefix: ")
if str1.startswith(prefix):
    print(f"{prefix} is prefix of string {str1}")
else:
    print(f"{prefix} is not a prefix of string {str1}")

suffix = input("Enter given suffix: ")
if str1.endswith(suffix):
    print(f"{suffix} is suffix of string {str1}")
else:
    print(f"{suffix} is not a suffix of string {str1}")
