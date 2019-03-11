num = list(map(str, input()))
num.sort(key=int, reverse=True)
print(''.join(num))
