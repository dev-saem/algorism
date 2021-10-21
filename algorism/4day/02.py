# 02. 돌다리 건너가기(DP)

t = int(input())
for i in range(t):
    n = int(input())
    # t[i] : i번째 돌다리에 도달하는 경우의 수
    t = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:  # if ~ elif : 초기값
            t[1] = 1
        elif i == 2:
            t[2] = 2
        elif i == 3:
            t[3] = 4
        else : # 점화식
            t[i] = (t[i-1] + t[i-2] + t[i-3]) %1904101441
    print(t[n])