def coin_change(value_list, change):
    min = 9999999
    #min = change
    if change in value_list:
        return 1
    else:
        for i in [c for c in value_list if c<=change]:
            change_times = 1 + coin_change(value_list, change - i)
            if change_times < min:
                min = change_times
    return min

print(coin_change([1, 5, 10, 25], 60)) 