from sys import stdin
from itertools import *

input = stdin.readline

n, m = map(int, input().split())
connect = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
    k, *s = list(map(int, input().split()))
    for j in s:
        connect[i][j-1] = 1

ps = list(map(int, input().split()))

onoff = (0, 1)
patterns = list(product(onoff, repeat=n))

ans = 0
for pattern in patterns:
    cnt = 0
    for i in range(m):
        sum = 0
        for j in range(n):
            sum += connect[i][j]*pattern[j]
        if sum % 2 == ps[i]:
            cnt += 1
        else:
            break
    if cnt == m:
        ans += 1

print(ans)
