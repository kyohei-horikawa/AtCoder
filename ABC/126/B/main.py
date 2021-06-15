from sys import stdin

input = stdin.readline
data = input()

s = int(data[:2])
e = int(data[2:])


def isMonth(month):
    if 0 < month and month < 13:
        return True
    else:
        return False


if isMonth(s):
    if isMonth(e):
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if isMonth(e):
        print('YYMM')
    else:
        print('NA')
