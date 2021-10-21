# 피보나치 수열

def fibo(n):
  if (n == 1) or (n == 2):
    return 1
  else:
    return fibo(n-2) + fibo(n-1)

t = int(input())
for i in range(t):
  n = int(input())
  print(fibo(n))

