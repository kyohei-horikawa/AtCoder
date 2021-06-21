from sys import stdin
input = stdin.readline

n = int(input().rstrip())

price = round(n*1.08)
if price < 206:
    print('Yay!')
elif price == 206:
    print('so-so')
else:
    print(':(')
