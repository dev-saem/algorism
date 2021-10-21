# 01. DFS

import sys
sys.setrecursionlimit(1000000)

t = int(input())
for n in range(t):
    N, M = map(int, input().split())
    List = [[] for m in range(N)]

    for i in range(M):
         u, v = map(int, input().split())
         List[u].append(v)
         List[v].append(u)
    
    for i in range(N):
        List[i].sort(reverse=True)
    
    check = [False]*(N)
    stack = [0]
    while stack:
        v = stack.pop()
        if check[v] == True:
            continue
        check[v] = True
        print(v, end = " ")
        
        for i in List[v]:
            if check[i] == False:
                stack.append(i)
    print("")