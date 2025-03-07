weights = [2,3,4,5,9]
values = [3,4,8,8,10]
n = 5
W = 20

def bag(weights,values,n,W,memo={}):
    if n==0 or W ==0:
        return 0
    if (W,n) in memo:
        return memo[(W,n)]
    
    elif weights[n-1]>W:
        memo[(W,n)] = bag(weights,values,n-1,W,memo)
    
    else:
        memo[(W,n)] = max(bag(weights,values,n-1,W,memo),
                          bag(weights,values,n-1,W-weights[n-1],memo) + values[n-1])
    return memo[W,n]

print(bag(weights,values,n,W,memo={}))