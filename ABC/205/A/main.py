from sys import stdin
input = stdin.readline

a, b = map(int, input().split())

cal = a/100
if cal % 10 == 0:
    print(int(cal*b))
else:
    print(cal*b)
