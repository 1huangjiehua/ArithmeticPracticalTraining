#n：物品件数；c:最大承重为c的背包；w:各个物品的重量；v:各个物品的价值
#第一步建立最大价值矩阵(横坐标表示[0,c]整数背包承重):(n+1)*(c+1)
#技巧:python 生成二维数组(数组)通常先生成列再生成行
def bag(n,c,w,p):
    res=[[-1 for j in range(c+1)]for i in range(n+1)]
    for j in range(c+1):
        #第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        res[0][j]=0
    for i in range(1,n+1):
        for j in range(1,c+1):
            res[i][j]=res[i-1][j]
            #生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if(j>=w[i-1]) and res[i-1][j-w[i-1]]+p[i-1]>res[i][j]:
                res[i][j]=res[i-1][j-w[i-1]]+p[i-1]
    return res
#以下代码功能：标记出有放入背包的物品
#反过来标记，在相同价值情况下，后一件物品比前一件物品的最大价值大，则表示物品i#有被加入到背包，x数组设置为True。设初始为j=c。
def show(n,c,w,res):  
    print('最大价值为:',res[n][c])  
    x=[False for i in range(n)]  
    j=c  
    for i in range(1,n+1):  
        if res[i][j]>res[i-1][j]:  
            x[i-1]=True  
            j-=w[i-1]  
    print ('选择的物品为:')
    for i in range(n):  
        if x[i]:  
            print ('第',i+1,'个,' )
    print('')
if __name__=='__main__':  
    n=5  
    c=10  
    w=[2,2,6,5,4]  
    p=[6,3,5,4,6]  
    res=bag(n,c,w,p)  
    show(n,c,w,res) 