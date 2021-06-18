from sys import stdin
input = stdin.readline
a = sorted(map(int, input().split()))

sum = 0
for i in range(2):
    sum += a[i]

print(sum)
