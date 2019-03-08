line = int(input())

for _ in range(line):
    ip = list(map(str, input().split(' ')))
    par = ''
    for l in list(ip[1]):
        par += l*int(ip[0])
    print(par)
