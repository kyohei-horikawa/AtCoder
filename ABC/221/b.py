import sys
import copy
input = sys.stdin.readline


def main():
    s = list(input().rstrip())
    t = input().rstrip()

    n = len(s)
    flag = False

    if ''.join(s) == t:
        flag = True

    for i in range(n):
        c = copy.copy(s)
        if i > 0:
            tmp = c[i]
            c[i] = c[i - 1]
            c[i - 1] = tmp
            if ''.join(c) == t:
                flag = True

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
