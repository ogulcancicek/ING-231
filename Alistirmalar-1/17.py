num = int(input('Lütfen bir değer giriniz: '))
if (num >= 100) and (num <= 9999):
    num = str(num)
    if num == num[::-1]:
        print(True)
    else:
        print(False)