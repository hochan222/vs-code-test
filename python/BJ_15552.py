import sys
count = sys.stdin.readline()
for _ in range(0, int(count)):
    num = sys.stdin.readline().split()
    print(int(num[0]) + int(num[1]))
