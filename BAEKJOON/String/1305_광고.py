# https://www.acmicpc.net/problem/1305

def advertisement(L, P):
    pi = [0] * len(P)
    j = 0

    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if (P[i] == P[j]):
            j += 1
            pi[i] = j

    return L - pi[-1]

L = int(input())
string = input()

print(advertisement(L, string))