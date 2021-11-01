# 1'den N'ye kadar olan sayıların çarpımını veren rekürsif fonksiyon
def recursion_prod(n):
    if n <= 1:
        return n # 1'den küçük eşit değerlerin kendisi döndürülür ve referans noktası oluşturulur.
    else:
        return n * recursion_prod(n-1)