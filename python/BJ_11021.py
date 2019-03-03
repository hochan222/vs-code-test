idx = int(input())

for i in range(idx):
    a = map(int, input().split())
    print('Case #{}: {}'.format(i+1, sum(a)))

