class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]

    def insert(self,item):
        self.heaplist.append(item)
        pos = len(self.heaplist)-1

        while pos//2 > 0:
            if self.heaplist[pos] < self.heaplist[pos//2]:
                temp = self.heaplist[pos//2]
                self.heaplist[pos//2] = self.heaplist[pos]
                self.heaplist[pos] = temp         
            pos = pos//2

    def delMin(self):
        self.heaplist[1] = self.heaplist[-1]
        self.heaplist.pop()
        pos = 1
        while pos * 2 < len(self.heaplist):

            left_idx = pos*2
            right_idx = pos*2+1

            left = self.heaplist[left_idx]
            right = self.heaplist[right_idx] if right_idx < len(self.heaplist) else float('inf')

            if left < right:
                smaller_idx = left_idx
                smaller_val = left
            else:
                smaller_idx = right_idx
                smaller_val = right
            
            if self.heaplist[pos] > smaller_val:
                tmp = self.heaplist[pos]
                self.heaplist[pos] = smaller_val
                self.heaplist[smaller_idx] = tmp
                pos = smaller_idx
            else:
                break

hplist = BinaryHeap()
hplist.insert(6)
hplist.insert(3)
hplist.insert(2)
hplist.insert(21)
hplist.insert(1)

print(hplist.heaplist)
hplist.delMin()
print(hplist.heaplist)