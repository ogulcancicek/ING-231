import math

sum = 0
inf = 10000000
for i in range(0,inf):
    sum += (1 / math.factorial(i))
print(sum)
