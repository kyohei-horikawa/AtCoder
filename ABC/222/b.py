import sys
input = sys.stdin.readline


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    fail_count = 0
    for i in range(n):
        if a[i] < p:
            fail_count += 1
    print(fail_count)


if __name__ == "__main__":
    main()
