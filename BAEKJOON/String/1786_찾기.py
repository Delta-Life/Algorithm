# https://www.acmicpc.net/problem/1786

def get_pi(P):
    pi = [0] * len(P)
    j = 0

    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if (P[i] == P[j]):
            j += 1
            pi[i] = j

    return pi

def KMN(T, P):
    pi = get_pi(P)
    j = 0
    result = []

    for i in range(0, len(T)):
        while j > 0 and T[i] != P[j]:
            j = pi[j-1]
        if T[i] == P[j]:
            if j == len(P) - 1:
                result.append(i - len(P) + 2)
                j = pi[j]
            else:
                j += 1
    
    return result

T = input()
P = input()

result = KMN(T, P)
print(len(result))
print(" ".join(map(str, result)))