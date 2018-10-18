def lcs(a, b):
    n = len(a)
    m = len(b)

    mean_len = (m+n)/2.0
    l = [[0]*(m+1) for i in range(n+1)]
    # l = [[0] * (m+1)] * (n+1)
    for i in range(n+1)[1:]:
        for j in range(m+1)[1:]:
            if a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    print l[-1][-1]
    print mean_len
    print l[-1][-1]/mean_len
    print l


l = [[0] * (7+1)] * (6+1)
ll = [[0]*(7+1) for i in range(6+1)]
lll = [0] * (7+1)
print l
print ll
print lll

a = 'BDCABA'
b = 'ABCBDAB'
lcs(a, b)

