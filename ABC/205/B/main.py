from sys import stdin
input = stdin.readline

n = int(input().rstrip())

exp = list(map(int, input().split()))
exp.sort()

ans = []
for i in range(1, n+1):
    ans.append(int(i))

if ans == exp:
    print('Yes')
else:
    print('No')
