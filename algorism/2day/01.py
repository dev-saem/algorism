# 01. 이진탐색 1

t = int(input())
for i in range(t):
  data = list(map(int, input().split()))
  query = list(map(int, input().split()))
  answer = []

  for q in query:
    start = 0
    end = len(data) - 1

    while start <= end:
      mid = (start + end) // 2
      if q == data[mid]:
        break
      elif q > data[mid]:
        start = mid + 1  
      elif q < data[mid]:
        end = mid - 1

    if end < start:
      answer.append(-1)
    else :
      answer.append(mid)

  print(*answer)