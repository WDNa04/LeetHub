import sys

def mergeAlternately(self, word1, word2):
    l1 = len(word1)
    l2 = len(word2)
    line = ""
    for i in range(min(l1, l2)):
        line += word1[i]
        line += word2[i]
    for i in range(min(l1, l2), max(l1, l2)):
        if max(l1, l2) == len(word1):
            line += word1[i]
        elif max(l1, l2) == len(word2):
            line += word2[i]
    return line

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()
print(mergeAlternately("self", word1, word2))
