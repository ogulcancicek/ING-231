for num in range(10000,100000):
    isPrime = True
    for i in range(2,num):
        if (num % i) == 0:
            isPrime = False
            break
    if isPrime:
        print(num)
