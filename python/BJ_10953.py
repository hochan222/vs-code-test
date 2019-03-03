index = int(input())

for i in range(index):
    a = list(map(int, input().split(',')))
    print(sum(a))

