# 03. 리스트의 합

t = int(input())
for i in range(t):
    li = input().split()
    s = 0

    for j in range(len(li)):
      s += int(li[j])
    print(s)