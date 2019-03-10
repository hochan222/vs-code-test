from functools import reduce
def f(acc, cur):
    if acc == cur:
        overlap.append(cur)
        return cur
    return cur

n = int(input())
overlap = []
count = 0

for i in range(n):
    word = input()
    reduce(f, word)
    word_set = set(word)
    if len(word_set) == len(word) - len(overlap):
        count += 1
    else:
        pass
    overlap = []

print(count)
