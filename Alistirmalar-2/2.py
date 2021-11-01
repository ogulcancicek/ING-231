# 1'den N'ye kadar olan sayıları rekürsif olarak toplama
def recursion_sum(n):
    if n <= 1: # 1'den küçük eşit değerlerin kendisi döndürülür ve referans noktası oluşturulur.
        return n
    else:
        return n + recursion_sum(n-1)