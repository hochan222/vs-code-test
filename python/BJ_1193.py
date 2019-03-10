n = int(input())
add = 1
while n > add:
    n = n - add
    add += 1
a = n
b = add - n + 1
if add % 2 == 1:
    a, b = b, a
print(str(a)+"/"+str(b))
