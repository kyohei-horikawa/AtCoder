import sys
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    flag = True
    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            flag = False
            break
    if flag:
        print(-1)


if __name__ == "__main__":
    main()
