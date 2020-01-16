UP_LEFT = 0  # 左上
UP = 1  # 上
LEFT = 2  # 左


def LCS(X, Y):
    '''
    输入：序列X和序列Y
    输出：X和Y的最长公共子序列长度
    '''
    # 定义f数组，每行n个元素，每列m个元素
    m = len(X)
    n = len(Y)
    # lf = (lambda x,y:x+1 if x>y else y+1)
    # size = lf(m,n)
    f = [[0 for x in range(n + 1)] for y in range(m + 1)]
    # 定义路径数组
    path = [[-1 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (X[i - 1] == Y[j - 1]):
                f[i][j] = f[i - 1][j - 1] + 1
                path[i][j] = UP_LEFT
            else:
                # f[i][j] = max(f[i-1][j],f[i][j-1])
                if (f[i - 1][j] > f[i][j - 1]):
                    f[i][j] = f[i - 1][j]
                    path[i][j] = UP
                else:
                    f[i][j] = f[i][j - 1]
                    path[i][j] = LEFT
    return f[m][n], path


def getpath(path, X, i, j, arr):
    '''
        回溯求子序列
        输入：path,二维数组，路径信息
            X，原始序列
            i,j ,递归下标
            arr，存储结果元素
    '''
    if (i == 0 or j == 0):
        return
    elif (path[i][j] == UP_LEFT):
        getpath(path, X, i - 1, j - 1, arr)
        arr.append(X[i - 1])
    elif (path[i][j] == UP):
        getpath(path, X, i - 1, j, arr)
    elif (path[i][j] == LEFT):
        getpath(path, X, i, j - 1, arr)
    else:
        pass


X = 'advSDWantage'
Y = 'educatiSDWonal'



arr = []
length, path = LCS(X, Y)
getpath(path, X, len(X), len(Y), arr)
print(length)
print(arr)