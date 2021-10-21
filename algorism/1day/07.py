import heapq

t = int(input())
for i in range(t):
  n = int(input())
  li = []

  for i in range(n):
    q = int(input())
    if q >= 1:
      heapq.heappush(li, q)
    elif q == -1:
      priority = heapq.heappop(li)
      print(priority)