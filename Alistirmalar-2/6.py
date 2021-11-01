# non-recursive binary search

def binary_search(liste: list,num):
    high = len(liste) -1
    low = 0
    mid = 0

    while high >= low:
        mid = (high + low) // 2
        if liste[mid] == num:
            return mid # Aranan değerin bulunduğu index'i return eder
        elif liste[mid] < num:
            low = mid + 1 # Aranan değer orta değerden büyük ise arama üst yarım parçada devam eder
        else:
            high = mid - 1 #  Aranan değer orta değerden küçük ise arama alt yarım parçada devam eder
    return -1
