def kpk(n):
    return n + sum(map(int, list(str(n))))


_self = {}
for i in range(1, 10001):
    if i not in _self:
        print(i)
    _self[kpk(i)] = 1

