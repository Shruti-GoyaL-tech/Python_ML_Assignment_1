temperature = int(input("Enter a value of temperature: "))

choice = int(input("Do you want to convert celcius to fahrenheit (1: Yes 0:No): "))

ans = 0

if choice:
    ans = (temperature * (9 / 5) + 32)
    print(f"{temperature} degree celcius is equivalent to {ans} degree fahrenheit")

choice = int(input("Do you want to convert fahrenheit to  celcius(1: Yes 0:No): "))
if choice:
    ans = (temperature - 32) * (5 / 9)
    print(f"{temperature} degree celcius is equivalent to {ans} degree fahrenheit")

