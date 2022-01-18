# https://www.acmicpc.net/problem/1543

def greedy_non_overlap_search(document, word):
    count, index = 0, 0

    while index < len(document) - len(word) + 1:
        if document[index:index+len(word)] == word:
            index += len(word)
            count += 1
        else:
            index += 1
    
    return count

document = input()
word = input()

print(greedy_non_overlap_search(document, word))
