import sys
from itertools import product, repeat
input = sys.stdin.readline


def main():
    n = list(map(int, input().rstrip()))
    max = -9999
    for pattern in list(product((0, 1), repeat=len(n))):
        a = []
        b = []
        for i, ele in enumerate(pattern):
            if ele:
                a.append(n[i])
            else:
                b.append(n[i])

        if not (len(a) == 0 or len(b) == 0):
            a = (''.join(map(str, sorted(a, reverse=True))))
            b = (''.join(map(str, sorted(b, reverse=True))))
            if max < int(a) * int(b):
                max = int(a) * int(b)

    print(max)


if __name__ == "__main__":
    main()
