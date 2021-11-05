def superPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return -1
    num = str(num)
    if len(num) > 1:
        new_num = int(num[:len(num)-1])
        return superPrime(new_num)

super_primes = []
for num in range(10000,100000):
    result = superPrime(num)
    if result != -1:
        super_primes.append(num)

print(super_primes)