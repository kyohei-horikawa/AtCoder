from sys import stdin
input = stdin.readline

a, p = map(int, input().split())

sum = 3*a+p

if sum % 2 == 0:
    print(sum//2)
else:
    print((sum-1)//2)
