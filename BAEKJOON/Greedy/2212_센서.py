# https://www.acmicpc.net/problem/2212

def get_reception_area(sensors, n, k):
    sensors.sort()
    
    for i in range(n-1, 0, -1):
        sensors[i] -= sensors[i-1]
    
    sensors.pop(0)
    sensors.sort()
    for i in range(k-1 if k < n else n-1):
        sensors.pop()
    
    return sum(sensors)

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

print(get_reception_area(sensors, n, k))