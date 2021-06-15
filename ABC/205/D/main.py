from sys import stdin
input = stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

arr = [i for i in range(1, 100)]

for i in a:
    arr.remove(i)

for i in range(q):
    k = int(input().rstrip())
    print(arr[k-1])
