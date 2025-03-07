#背包问题
#大盗潜入博物馆，面前有五件宝物，分别有重量和价值，大盗的背包仅能负重20公斤，如何选择宝物，总价值最高。
#item  weight  value
#1       2       3
#2       3       4
#3       4       8
#4       5       8
#5       9       10

#将m(i,W)记为：前i个宝物中，组合不超过W重量，得到的最大价值
#m(i,W)应该是m(i-1,W)和m(i-1,W-Wi)+vi的最大值
#从m(1,1)开始计算到m(5,20)

#[weight,value]
treasure = [None,[2,3],[3,4],[4,8],[5,8],[9,10]]
max_w = 20
m = {(i,w):0 for i in range(0,len(treasure)) for w in range(0,max_w+1)}

for i in range(1,len(treasure)):
    for w in range(1,max_w+1):
        if treasure[i][0] > w:
            m[(i,w)] = m[(i-1,w)]
        else:
            m[(i,w)] = max(m[i-1,w], treasure[i][1] + m[(i-1, w - treasure[i][0])])

print(m[(5,20)])