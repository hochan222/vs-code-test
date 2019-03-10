n = int(input())
total = 1
dist = 1
while total < n:
    total += dist * 6
    dist += 1
print(dist)
