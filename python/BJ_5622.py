arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
count = 0

for i in word:
    for k in arr:
        if i in k:
            count += arr.index(k) + 3
print(count)
