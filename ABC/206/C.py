from sys import stdin
from math import factorial
input = stdin.readline

n = int(input().rstrip())

a = list(map(int, input().split()))
a.sort()

con = int(factorial(n) / factorial(2) / factorial(n - 2))

sum = 0
for i in range(a[0], a[-1]+1):
    if a.count(i) >= 2:
        sum += int(a.count(i)*(a.count(i)-1)/2)

print(con-sum)
