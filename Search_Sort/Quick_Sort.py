def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        left =  [x for x in list[1:] if x <= pivot]
        right = [x for x in list[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
print(quick_sort([5,1,2,43,5,2,4,34]))