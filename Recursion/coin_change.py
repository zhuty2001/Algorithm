# 硬币找零问题
# 问题描述：给定一组硬币，每个硬币有一个面值，给定一个找零的数值，找出最少的硬币数目
# 例如：硬币面值为[1, 5, 10, 25]，找零为60，最少硬币数目为3（25+25+10）
#
# 递归思想：
# 1.找零数值等于硬币面值，返回1
# 2.找零数值大于硬币面值，找零数值减去硬币面值，递归调用

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

print(coin_change([1, 5, 10, 25], 58)) 