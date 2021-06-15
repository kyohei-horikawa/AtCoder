from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())


def abs(num):
    if num > 0:
        return num
    else:
        return -num


def judge(a, b):
    if abs(a) == abs(b):
        print('=')
    elif abs(a) > abs(b):
        print('>')
    elif abs(a) < abs(b):
        print('<')
    else:
        print('=')


if c % 2 == 0:
    judge(a, b)
else:
    if a == b:
        print('=')
    elif a > 0 and b > 0:
        judge(a, b)
    elif a > 0 and b < 0:
        print('>')
    elif a < 0 and b > 0:
        print('<')
    else:
        if a > b:
            print(">")
        else:
            print('<')
