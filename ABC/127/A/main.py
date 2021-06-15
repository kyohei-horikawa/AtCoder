from sys import stdin

input = stdin.readline

A, B = input().split(' ')

if int(A) >= 13:
    print(B)
elif int(A) <= 5:
    print(0)
else:
    print(round(int(B)/2))
