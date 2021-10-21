# 06. 큐 구현

import collections

t = int(input())
for i in range(t):
  n = int(input())
  li = collections.deque([])

  for i in range(n):
    q = int(input())
    if q >= 1:
      li.append(q)
    elif q == -1:
      first = li.popleft()
      print(first)