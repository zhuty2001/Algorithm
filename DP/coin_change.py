#依靠前一步的最优解找到这一步的最优解

def coin_change(value_list, change, mintime_list):
    for i in range(1, change+1):
        min = 99999
        for j in [c for c in value_list if c <= i ]:
            if mintime_list[i-j] + 1 < min:
                mintime_list[i] = mintime_list[i-j] + 1
                min = mintime_list[i-j] + 1
    return mintime_list[change]

print(coin_change([1,5,10,21,25], 63, [0]*64))