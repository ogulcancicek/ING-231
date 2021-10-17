for num in range(1,2006):
    sum_of_digits = 0
    for digit in list(str(num)):
        sum_of_digits += int(digit)
    if sum_of_digits == (2005 - num):
        print(num)