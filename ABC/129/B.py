from sys import stdin
import numpy as np
input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))

s = np.cumsum(a)
sum = s[-1]


def abs(num):
    if num < 0:
        return -num
    else:
        return num


min = 99999999
for i in range(n - 1):
    if abs(s[i] - (sum - s[i])) < min:
        min = abs(s[i] - (sum - s[i]))

print(min)
