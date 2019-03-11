num = int(input())
arr = []
[arr.append(input()) for _ in range(num)]
arr = sorted(set(arr), key=lambda v: (len(v), v))
[print(arr[i]) for i in range(len(set(arr)))]
