word = input().upper()

arr = sorted(list(map(lambda v: (v, word.count(v)), set(word))), key=lambda v: v[1])[::-1]
if len(arr) == 1:
    print(arr[0][0])
elif arr[0][1] == arr[1][1]:
    print('?')
else:
    print(arr[0][0])
