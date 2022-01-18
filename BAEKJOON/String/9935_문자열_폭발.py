# https://www.acmicpc.net/problem/9935

def string_explosion(str1, str2):
    last_char = str2[-1]
    stack = []
    length = len(str2)
 
    for char in str1:
        stack.append(char)
        if char == last_char and ''.join(stack[-length:]) == str2:
            del stack[-length:]
 
    result = ''.join(stack)
 
    if result == '':
        return "FRULA"
    else:
        return result

str1 = input()
str2 = input()

print(string_explosion(str1, str2))