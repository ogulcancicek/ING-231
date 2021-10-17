min_diff = 121211
min_values = list()
for i in range(1,121213):
    if 121212 % i == 0:
        values = [i,(121212 // i)]
        diff = max(values) - min(values)
        if diff < min_diff:
            min_diff = diff
            min_values = [i,(121212 // i)]

print(min_values)