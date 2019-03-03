import sys
c = int(sys.stdin.readline())
average = 0

for i in range(c):
    average = 0
    arr = list(map(int, sys.stdin.readline().split()))
    for n in range(arr[0]):
        average += arr[n+1]
    average /= arr[0]
    print('{0:.3f}%'.format(len(list(filter(lambda v: v > average, arr[1:])))/arr[0]*100))

