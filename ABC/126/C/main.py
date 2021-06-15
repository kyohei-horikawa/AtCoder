from sys import stdin
input = stdin.readline

N, K = input().split(' ')
N = int(N)
K = int(K)

res = 0

for i in range(N):
    score = i+1
    if 1 <= score and score < + K-1:
        count = 0
        while(score <= K):
            score *= 2
            count += 1
        res += (1/N)*(0.5)**count
    else:
        res += (1/N)

print(f'{res:.12f}')
