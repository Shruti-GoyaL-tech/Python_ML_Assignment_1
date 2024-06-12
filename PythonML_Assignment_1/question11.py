n = int(input("Enter size of fibonacci series: "))
fibonacci_list = [0, 1]
for i in range(2, n):
    fibonacci_list.append(fibonacci_list[-1]+ fibonacci_list[-2])

print(f"The Fibonacci series id {fibonacci_list}")
