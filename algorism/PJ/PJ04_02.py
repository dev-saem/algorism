# 02. 세계 암기대회

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
        
    t = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                t[i][j] = data[i][j]
            elif i == 0:
                t[i][j] = t[i][j-1] + data[i][j]
            elif j == 0:
                t[i][j] = t[i-1][j] + data[i][j]
            else:
                t[i][j] = min(t[i][j-1], t[i-1][j], t[i-1][j-1]) + data[i][j]
    print(t[n-1][m-1])