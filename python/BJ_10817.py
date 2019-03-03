import sys
score = sys.stdin.readline().split()
score.sort(key=int)
print(score[1])
