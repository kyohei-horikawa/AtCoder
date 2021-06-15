from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

cards = [int(i) for i in input().split()]
cards = sorted(cards)
max = -999999

for i in range(M):
    B, C = map(int, input().split())
    for j in range(B):
        if cards[j] < C:
            cards[j] = C
    if max < sum(cards):
        max = sum(cards)

print(max)
