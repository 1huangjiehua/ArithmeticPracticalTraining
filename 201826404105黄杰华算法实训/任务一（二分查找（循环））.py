
def erfenfa(lis, nun):
    left = 0
    right = len(lis) - 1
    while left <= right: #循环条件
        mid = (left + right) // 2 #获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]: #如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1 #来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]: #如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1 #来到右边后，需要将左边的边界换为mid+1
        else:
            return mid #如果查询数字刚好为中间值，返回该值得索引
    return -1 #如果循环结束，左边大于了右边，代表没有找到


lis = [15,58,68,94,12,45,35,36,14,54]
print(lis)
lis.sort()
print(lis)
while 1:
    num = int(input('输入要查找的数：'))
    res = erfenfa(lis, num)
    print(res)
    if res == -1:
        print('未找到！')
    else:
        print('找到！')

