n = int(input())
a = [0]*1000000
count = 0
for i in range(n):
    a[int(input())] = 1
for i in range(n):
    if count + i == 1000000:
        break
    if a[i+count] == 0:
        del a[i+count]
        count += 1
print(a)