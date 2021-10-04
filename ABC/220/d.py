import sys
import itertools
import copy
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    iterable = [0, 1]
    pattern = list(itertools.product(iterable, repeat=n - 1))
    for i in range(10):
        res = []
        for j in pattern:
            b = copy.copy(a)
            for k in j:
                if k:
                    f(b)
                else:
                    g(b)
            res.append(b[0])
        print(res.count(i))


def f(array):
    x = array.pop(0)
    y = array.pop(0)
    array.insert(0, (x + y) % 10)
    return array


def g(array):
    x = array.pop(0)
    y = array.pop(0)
    array.insert(0, (x * y) % 10)
    return array


if __name__ == "__main__":
    main()
