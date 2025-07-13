def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Get user input
n = int(input("Enter the number of terms in the Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series up to", n, "terms:")
    print(fibonacci_series(n))
