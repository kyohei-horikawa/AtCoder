from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

maxl, minr = map(int, input().split())

for i in range(M-1):
    l, r = map(int, input().split())
    if maxl < l:
        maxl = l
    if minr > r:
        minr = r

print(max(0, minr-maxl+1))
