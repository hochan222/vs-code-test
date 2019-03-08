alpha = [0]*26
count = 0
num = int(input())
for k in range(num):
    word = input()+' '
    for i in list(word):
        if i == ' ':
            break
        elif i == word[i+1]:
            word[i] = ' '
    print(word)
