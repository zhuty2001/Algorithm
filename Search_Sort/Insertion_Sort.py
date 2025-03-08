def insertion_sort(list):
    for i in range(1,len(list)):
        current_item = list[i]
        pos = i
        while list[pos-1] > current_item and pos > 0:
            list[pos] =  list[pos-1]
            pos = pos - 1
        list[pos] = current_item
    return list

print(insertion_sort([2,6,1,2,6,7]))