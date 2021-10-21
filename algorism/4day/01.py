# 01. 세금징수(그리디)

t = int(input())
for i in range(t):
    n = int(input())
    coins = [50000, 10000, 5000, 1000, 500, 100]
    coinnum = 0
    for coin in coins:
        coinnum += n // coin
        n %= coin
    print(coinnum)