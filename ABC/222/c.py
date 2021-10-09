import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    rank = {}
    for i in range(2 * n):
        rank[i + 1] = [0, list(input().rstrip())]

    print(rank)

    for i in range(m):
        for j in range(1, n + 1):
            jyanken(rank[2 * j - 1], rank[2 * j])
        rank = sorted(sorted(rank.items(), key=lambda x: x[1][0], reverse=True))
        print(rank)

    print(rank)


def jyanken(a, b):

    hand1 = a[1].pop(0)
    hand2 = b[1].pop(0)

    if hand1 == 'G' and hand2 == 'C':
        a[0] += 1
    elif hand1 == 'C' and hand2 == 'P':
        a[0] += 1
    elif hand1 == 'P' and hand2 == 'G':
        a[0] += 1
    elif hand1 == 'G' and hand2 == 'G':
        pass
    elif hand1 == 'C' and hand2 == 'C':
        pass
    elif hand1 == 'P' and hand2 == 'P':
        pass
    elif hand1 == 'G' and hand2 == 'P':
        b[0] += 1
    elif hand1 == 'C' and hand2 == 'G':
        b[0] += 1
    elif hand1 == 'P' and hand2 == 'C':
        b[0] += 1


if __name__ == "__main__":
    main()
