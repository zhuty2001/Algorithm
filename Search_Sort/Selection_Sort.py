def selection_sort(list):
    for i in range(len(list)-1,0,-1):
        largest_pos = 0
        for j in range(i+1):
            if list[j] > list[largest_pos]:
                largest_pos = j
        temp = list[i]
        list[i] = list[largest_pos]
        list[largest_pos] = temp
    return list

print(selection_sort([32,4,1,21]))
            


