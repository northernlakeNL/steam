def searchboi(value, lst):
    low = 0
    high = len(lst) -1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if value <= lst[mid]:
            high = mid
        else:
            low = mid
        if low == high:
            return True
        elif low+1 == high:
            return lst[high] == value or lst[low] == value




def find(L, target):
    start = 0
    end = len(L) - 1
    L.sort()
    print(L)
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint

L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"] # Needs to be sorted.

lijst =  ['invoering', 'actueel', 'gefinancierd', 'seksisme', 'hoger', 'afwerken', 'contract', 'entameren', 'bestudering', 'groeve']
value = 'seksisme'

print(find(lijst, value))


print(find(L, "Lois"))