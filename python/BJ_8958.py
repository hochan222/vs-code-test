n = int(input())
count = 0
plus = 0

for i in range(n):
    correct = input()
    for k in range(len(correct)):
        if correct[k] == 'O':
            plus += 1
        elif correct[k] == 'X':
            plus = 0
        count += plus
    print(count)
    count = 0
    plus = 0
