start = 10000
end = 100000
counter = 0
for num in range(start,end):
    first_couple = num // 1000 
    last_couple = num % 100
    if first_couple == last_couple:
        counter += 1
        
print(counter)