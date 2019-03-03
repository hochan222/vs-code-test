def next_num(v):
    p = v // 10
    q = v % 10
    return q * 10 + (p + q) % 10


n = int(input())
m = n
count = 0
while count == 0 or n != m:
    m = next_num(m)
    count += 1
print(count)
