# https://www.acmicpc.net/problem/1461

def library(books, m):
    left = [book for book in books if book < 0]
    right = [book for book in books if 0 < book]
    right.sort(reverse=True)
    left.sort()
    max_distance = max(map(abs, books))

    distance = max_distance
    for i in range(0, len(right), m):
      if right[i] != max_distance:
        distance += right[i] * 2

    for i in range(0, len(left), m):
      if -left[i] != max_distance:
        distance -= left[i] * 2

    return distance

n, m = map(int, input().split())
books = list(map(int, input().split()))

print(library(books, m))