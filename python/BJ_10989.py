import sys
num = int(sys.stdin.readline())
dic = {}

for _ in range(num):
    v = int(sys.stdin.readline())
    if v in dic:
        dic[v] += 1
    else:
        dic[v] = 1

for i in sorted(dic.items(), key=lambda k: k[0]):
    [print(i[0]) for _ in range(i[1])]
