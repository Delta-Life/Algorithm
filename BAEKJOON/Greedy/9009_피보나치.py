# https://www.acmicpc.net/problem/9009

def fibo_sum(n, fibo):
    result = []
    for k in range(45, -1, -1):
        if(fibo[k]<=n):
            n -= fibo[k]
            result.append(fibo[k])
    return result[::-1]

fibo = [1,2] + [0] * 44
for i in range(2, 46):
    fibo[i] = fibo[i-2]+fibo[i-1]

t = int(input())

for j in range(t):
    n = int(input())
    print(" ".join(map(str, fibo_sum(n, fibo))))