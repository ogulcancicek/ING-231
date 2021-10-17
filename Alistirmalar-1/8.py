counter = 0
for num in range(100,1000):
    if num % 2 != 0:
        continue
    else:
        a = num // 100
        b = (num // 10) % 10
        c = num % 10
        if (a == b) or (b == c) or (a == c) or (a == b == c):
            counter += 1
            print(num)
print('-'*15)
print(counter)