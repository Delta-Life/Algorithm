# https://www.acmicpc.net/problem/11508

def get_min_cost(n, costs):
    costs.sort(reverse=True)
    result = sum([costs[i] + costs[i+1] for i in range(0, n-2, 3)])
    result += sum(costs[n%3*(-1):]) if n % 3 != 0 else 0
    return result

n = int(input())
costs = [int(input()) for _ in range(n)]

print(get_min_cost(n, costs))