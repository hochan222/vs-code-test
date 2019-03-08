total = []
for _ in range(5):
    score = int(input())
    if score < 40:
        total.append(40)
    else:
        total.append(score)
print(int(sum(total)/5))
