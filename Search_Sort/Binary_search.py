#O(n) = log(n)
#2^i = n

def binary_search(list, item):
    first = 0
    last = len(list)-1
    found = False
    while first != last:
        mid = (first+last) // 2
        if list[mid] == item:
            return True
        elif list[mid] < item:
            first = mid + 1
        elif list[mid] > item:
            last = mid - 1
    return found

def binart_search_recursion(list,item):
    if list == []:
        return False
    else:
        mid = (len(list)-1) // 2
        if item == list[mid]:
            return True, item
        if list[mid] < item:
            return binart_search_recursion(list[mid+1:],item)
        elif list[mid] > item:
            return binart_search_recursion(list[:mid],item)

print(binary_search([1,4,8,15,26],8))
print(binart_search_recursion([1,4,8,15,26,30],4))

