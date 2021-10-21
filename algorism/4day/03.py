# 03. 암기대회

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    # t[i][j] : (0,0)에서 (i,j)에 도달했을 때 얻을 수 있는 최대 점수
    t = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:   # 시작 칸인 경우 : 자기자신
                t[i][j] = data[i][j]
            elif i == 0:    # 제일 위쪽 줄인 경우 왼쪽에서밖에 올 수 없다
                t[i][j] = t[i][j-1] + data[i][j]
            elif j == 0:    # 제일 왼쪽 줄인 경우 위쪽에서밖에 올 수 없다
                t[i][j] = t[i-1][j] + data[i][j]
            else:   # 그 외의 경우
                t[i][j] = max(t[i][j-1], t[i-1][j]) + data[i][j]
    print(t[n-1][m-1])