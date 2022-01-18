# https://www.acmicpc.net/problem/1026

_ = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

A.sort()
B.sort()

for n, i in enumerate(B[::-1]):
    sum += A[n] * i

print(sum)