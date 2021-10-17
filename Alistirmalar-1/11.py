max_val = 0
for i in range(1,126):
    if (125 % i) == (200 % i) == (350 % i):
        if i > max_val:
            max_val = i
print(max_val)