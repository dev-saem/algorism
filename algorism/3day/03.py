# 03. BFS

from collections import deque

t = int(input())
for n in range(t):
    N, M = map(int, input().split())
    List = [[] for m in range(N)]

    for i in range(M):
         u, v = map(int, input().split())
         List[u].append(v)
    
    for i in range(N):
        List[i].sort()
    
    check = [False]*N
    queue = deque([0])
    while queue:
        v = queue.popleft()
        if check[v] == True:
            continue
        check[v] = True
        print(v, end = " ")
        
        for i in List[v]:
            if check[i] == False:
                queue.append(i)  