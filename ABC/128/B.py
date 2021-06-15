from sys import stdin
input = stdin.readline

n = int(input().rstrip())

book = {}
for i in range(1, n+1):
    city, score = input().split()
    score = int(score)
    if city not in book.keys():
        book[city] = {}
    book[city][i] = score

book_sorted = sorted(book.items(), key=lambda x: x[0])

for ele in book_sorted:
    score_sorted = sorted(ele[1].items(), key=lambda x: x[1], reverse=True)
    for val in score_sorted:
        print(val[0])
