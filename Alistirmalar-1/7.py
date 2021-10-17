counter = 0
for num in range(100,1000):
    num = str(num)
    if int(num[0]) + int(num[1]) == int(num[-1]):
        print(num)
        counter += 1
        
print("-"*15)
print(counter)