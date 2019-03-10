n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
for k in range(len(arr)):
    print(arr[k])
