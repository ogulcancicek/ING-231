num = int(input('Lütfen bir sayı giriniz: '))
isPrime = True
if num > 1:
    for i in range(2,num):
            if (num % i) == 0:
                isPrime = False
                break
    print(isPrime)