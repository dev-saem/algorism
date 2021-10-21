# 01. 무거운 용액

def cmp(x):
    return x[0] / x[1]
t = int(input())
for _ in range(t):
    N, C = map(int, input().split())
    liquidlist = []
    for i in range(N):
        liquidlist.append(tuple(map(int, input().split())))
    liquidlist.sort(key = cmp, reverse = True)
    maxg = 0
    for i in range(N):
        if C - liquidlist[i][1] >= 0:
            maxg += liquidlist[i][0]
            C -= liquidlist[i][1]
        else:
            maxg += (liquidlist[i][0] * C) / liquidlist[i][1]
            break
    print(int(maxg))