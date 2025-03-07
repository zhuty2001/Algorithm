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

print(binary_search([1,4,8,15,26],8))
