# coding=utf-8
def lcs(a, b):
    # a字符的长度
    n = len(a)
    # b字符的长度
    m = len(b)
    # 声明一个二维数组默认值全部为0
    # 外层长度为 a（n）字符的长度+ 1
    # 内层长度为 b（m）字符的长度+ 1
    # data[n][m] 即 n行m列
    l = [[0]*(m+1) for i in range(n+1)]

    # 从1开始循环到n+1行
    # 从1开始循环到m+1列

    # 如果相同，则取对角数值+1
    # 如果不相同，则取对角右和下的最大值
    for i in range(n+1)[1:]:
        for j in range(m+1)[1:]:
            if a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    print
    for data in l:
        print data

a = 'BDCABA'
b = 'ABCBDAB'
lcs(a, b)

