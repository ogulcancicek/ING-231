import random

num = random.randint(10,98)

while str(num)[0] == str(num)[1]: 
    # Tutulan sayı, basamakları farklı bir değer olana kadar işlem tekrarlanır.
    num = random.randint(10,98) 
    print(num)

nonFound = True

while nonFound:
    user_input = int(input('-> Lütfen bir değer girin:')) # Kullanıcı yukarıda tutulan sayı hakkında bir tahmin yapar.
    
    dogru_yer = yanlis_yer = 0

    if (user_input < 10) or (user_input > 98) or (user_input % 11 == 0):
        print("10 ile 98 arası bir tam sayı girmeniz gerekir ve girdiğiniz değerin basamakları aynı.")
    else:
        if user_input == num:
            print(f"Doğru tahmin {num}")
            nonFound = False # Kullanıcın tahmini ile bilgisayar tarafından tutulan değer aynı ise while döngüsü kırılır.
        else:
            if (str(user_input)[0] == str(num)[0]) or (str(user_input)[1] == str(num)[1]):
                dogru_yer += 1
            if (str(user_input)[0] == str(num)[1]) or (str(user_input)[1] == str(num)[0]):
                yanlis_yer -= 1
            print(f"Dogru Yer:{dogru_yer} | Yanlış Yer:{yanlis_yer}")