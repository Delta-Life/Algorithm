'''

https://www.acmicpc.net/problem/11726

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

def get_num_of_case(num):
    min_array = [1, 2]
    for i in range(2, num):
        min_array.append((min_array[i-1] + min_array[i-2]) % 10007)
    return min_array[num-1]

n = int(input())
print(get_num_of_case(n))