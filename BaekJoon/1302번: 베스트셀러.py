N = int(input())

book_list = dict()
for _ in range(N):
    b = input()
    if b not in book_list:
        book_list[b] = 0
    book_list[b] += 1

m = 0
answer = ""
for key in sorted(book_list.keys()):
    if book_list[key] > m:
        m = book_list[key]
        answer = key
print(answer)
