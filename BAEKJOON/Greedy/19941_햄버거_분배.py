# https://www.acmicpc.net/problem/19941

n, k = map(int, input().split())
string = list(input().rstrip())
count = 0

for i in range(len(string)):
    if string[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j < n and string[j] == "H":
                count += 1
                string[j] = "-"
                break

print(count)