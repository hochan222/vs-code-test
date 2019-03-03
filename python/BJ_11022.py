idx = int(input())

for i in range(idx):
    a = list(map(int, input().split()))
    print('Case #{}: {} + {} = {}'.format(i+1, a[0], a[1], sum(a)))
