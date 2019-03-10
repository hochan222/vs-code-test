ip = list(map(str, input().split(' ')))
print(max(ip[0][::-1], ip[1][::-1]))
