# 02. 두 바퀴 레이스

import collections

def race(car):
    li = collections.deque([]) # 큐의 형식
    for n in car:
        if n not in li:
            li.append(n)
        else :
            n_pop = li.popleft()
            if n_pop != n:  # n_pop과 넣는 n의 비교
                return "YES"
    if len(li) == 0:    # 빈 리스트일 때
        return "NO"
    return "YES"

t = int(input())
for i in range(t):
    car = list(map(int, input().split())) # 리스트의 형태로 입력
    print(race(car))