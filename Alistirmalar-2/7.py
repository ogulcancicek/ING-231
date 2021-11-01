# Recursive Binary Search

def binary_search(liste: list,high,low,num):
    if high >= low:
        mid = (high + low) // 2
        if liste[mid] == num:
            return mid
        elif liste[mid] < num:
            lowUpdated = mid + 1
            return binary_search(liste,high,lowUpdated,num)
        else:
            highUpdated = mid - 1
            return binary_search(liste,highUpdated,low,num)
    
    return -1