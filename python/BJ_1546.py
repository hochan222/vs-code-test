import sys
n = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
print((sum(arr)/max(arr)*100)/n[0])
