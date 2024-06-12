user_data = []
while True:
    data = str(input("Enter data: "))
    if data:
        user_data.append(data)
    else:
        break

for data in user_data:
    print(data)
