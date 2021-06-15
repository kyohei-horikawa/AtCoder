from sys import stdin
input = stdin.readline

r, D, x_2000 = map(int, input().split())

for i in range(10):
    print(x_2000*r-D)
    x_2000 = x_2000*r-D
