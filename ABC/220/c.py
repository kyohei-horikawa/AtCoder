import numpy
import sys
import math
input = sys.stdin.readline


def main():
    input()
    a = list(map(int, input().split()))
    s = numpy.sum(a)
    x = int(input())
    a = a * math.ceil((x / s))
    for i, sum in enumerate(numpy.cumsum(a)):
        if sum >= x:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
