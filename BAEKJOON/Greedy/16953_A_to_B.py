'''


https://www.acmicpc.net/problem/16953

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
1. 2를 곱한다.
2. 1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
'''

def greedy_min_cal(A, B):
    count = 1
    while A != B and (B % 2 == 0 or B % 10 == 1) and B > 0:
        if B % 10 == 1:
            B //= 10
        else:
            B //= 2
        count += 1
    return count if A == B else -1


A, B = map(int, input().split())
print(greedy_min_cal(A, B))
