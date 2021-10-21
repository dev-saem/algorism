# 04. 최댓값과 최솟값의 차이

def Max(li):
  max_i = li[0]
  for i in range(len(li)):
    if li[i] > max_i:
      max_i = li[i]
  return max_i

def Min(li):
  min_i = li[0]
  for i in range(len(li)):
    if li[i] < min_i:
      min_i = li[i]
  return min_i

t = int(input())
for i in range(t):
  li = list(map(int, input().split()))
  print(Max(li) - Min(li))