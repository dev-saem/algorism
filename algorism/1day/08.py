# 08. 하노이 탑

def Hanoi(n, start, mid, end):
  if n == 1:
    print(start + ' -> ' + end)
    return
    
  Hanoi(n-1, start, end, mid)
  print(start + ' -> ' + end)
  Hanoi(n-1, mid, start, end)
    
t = int(input())
for i in range(t):
  n = int(input())
  Hanoi(n, 'A', 'B', 'C')