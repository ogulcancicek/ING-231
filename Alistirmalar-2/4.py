def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for num in range(30):
    fibo = fibonacci(num)
    print(fibo, end=" ")