import sys
n, x = map(str, sys.stdin.readline().split())
arr = list(map(str, sys.stdin.readline().split()))

print(' '.join(list(filter(lambda v: int(v) < int(x), arr))))
