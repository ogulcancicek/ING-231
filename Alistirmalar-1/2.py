sum = 0
inf = 1000000

for i in range(1,inf):
    sum += (1/i**2)

pi_approx = (6 * sum)**(1/2)
print(pi_approx)