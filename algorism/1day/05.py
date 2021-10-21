# 05. 스택 구현

t = int(input())
for i in range(t):
  n = int(input())
  li = []

  for i in range(n):
    q = int(input())

    if q >= 1:
      li.append(q)
    elif q == -1:
      last = li.pop(q)
      print(last)