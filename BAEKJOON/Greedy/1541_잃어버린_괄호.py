# https://www.acmicpc.net/problem/1541

def greedy_sum(string):
    result = 0
    string = string.split('-')
    result += sum(map(int, string[0].split('+')))
    for i in string[1:]:
        result -= sum(map(int, i.split('+')))
    
    return result

string = input()
print(greedy_sum(string))