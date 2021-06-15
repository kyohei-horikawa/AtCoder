from sys import stdin

input = stdin.readline

n, order = input().split(' ')
ss = input().rstrip()

res = ''
for i, s in enumerate(ss):
    if i+1 == int(order):
        res += s.lower()
    else:
        res += s

print(res)
