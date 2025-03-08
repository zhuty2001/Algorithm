#O(n^2)
def bubble_sort(list):
    for i in range(len(list)):
        last_item = len(list)- 1 - i
        for j in range(last_item):
            print(j)
            temp = 0
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

print(bubble_sort([54,26,93,24,51,16,514,1,23]))