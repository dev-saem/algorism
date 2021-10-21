# 01. 이진탐색 2

def binary2(l, x):
    if x <= l[0]:
        return l[0]
    if x >= l[-1]:
        return l[-1]
    start = 0
    end = len(l)

    while start < end:
        mid = (start + end) // 2
        if x == l[mid]: # 입력한 리스트의 값과 mid의 값이 동일할 때, mid값 리턴
            return l[mid]
        elif x > l[mid]:    # 입력한 리스트의 값이 mid 값보다 클 때, 왼쪽 값 지움
            start = mid + 1
        elif x < l[mid]:
            end = mid   # 입력한 리스트의 값이 mid 값보다 작을 때, 오른쪽 값 지움
    if abs(l[end-1]-x) <= abs(l[end]-x):
        return l[end-1]
    else:
        return l[end]

t = int(input())
for i in range(t):
  l = list(map(int, input().split()))
  q = list(map(int, input().split()))
  ans = [binary2(l, x) for x in q]
  print(*ans)