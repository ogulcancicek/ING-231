counter = 0
for num in range(1000,10000):
    num = str(num)
    if num[0] > num[-1]:
        counter += 1
print(counter)