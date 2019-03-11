import math
import sys
num = int(sys.stdin.readline())
arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline()))
# int 로 정렬
arr.sort()
print(round(sum(arr) / len(arr)))
print(arr[math.floor((len(arr)-1)/2)])
print(sorted(list(map(lambda v: (v, arr.count(v)), set(arr))), key=lambda v: v[0])[1][0])
print(abs(arr[0]-arr[len(arr)-1]))
