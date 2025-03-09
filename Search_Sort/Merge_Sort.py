def merge_sort(list):
    if len(list) <=1:
        return list

    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(left if left else right)

    return merged

print(merge_sort([1,5,1,2,3,5,12,54,2]))