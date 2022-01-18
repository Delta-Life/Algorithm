# https://www.acmicpc.net/problem/12904

def a_and_b(s, t):
    while len(s) != len(t):
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]
    
    if s == t:
        return 1
    else:
        return 0

s = input()
t = input()

print(a_and_b(s, t))