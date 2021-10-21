01. 합병

def merge():
  N = list(map(int, input().split()))
  M = list(map(int, input().split()))
  li = []
  i = j = 0
	
  # N&M이 남아있을 때, 비교해서 작은 것부터 추가
  while i < len(N) and j < len(M):
    if N[i] <= M[j]:
      N[i] = 1
      li.append(N[i])
      i += 1
    else :
      M[j] = 2
      li.append(M[j])
      j += 1

  # N만 남아있을 때
  while i < len(N):
    N[i] = 1
    li.append(N[i])
    i += 1

  # M만 남아있을 때
  while j < len(M):
    M[j] = 2
    li.append(M[j])
    j += 1
  return li

t = int(input())
for i in range(t):
  res = merge()
  for i in range(len(res)):
    print(res[i], end = ' ')
  print("")