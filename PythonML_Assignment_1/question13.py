birth_year = int(input("Enter your year of birth: "))
current_year = int(input("Enter your current year: "))
if current_year < birth_year:
    print("Invalid data")
else:
    age = current_year - birth_year
    print(f"Your age is {age}")
