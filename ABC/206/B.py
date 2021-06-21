from sys import stdin
input = stdin.readline

n = int(input().rstrip())

sum = 0
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(1, n):
        sum += i
        if sum >= n:
            print(i)
            break
