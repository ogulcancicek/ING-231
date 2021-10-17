for num1 in range(10,100):
    for num2 in range(10,100):
        num3 = int(str(num1) + str(num2))
        
        if (num1 + num2)*11 == num3:
            print(f'Num1:{num1}')
            print(f'Num2:{num2}')