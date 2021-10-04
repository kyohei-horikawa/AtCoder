import sys
input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    diff = a - b
    print(32 ** diff)


if __name__ == "__main__":
    main()
