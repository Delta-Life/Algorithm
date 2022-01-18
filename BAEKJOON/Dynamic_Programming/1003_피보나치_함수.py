# https://www.acmicpc.net/problem/1003

def fibo(num):
    tmp = [0, 1, 0, 1, 1]
    for i in range(5, num+3):
        tmp.append(tmp[i-1] + tmp[i-2])
    
    return tmp[num+1], tmp[num+2]

T = int(input())
    
for _ in range(T):
    print(' '.join(map(str, fibo(int(input())))))