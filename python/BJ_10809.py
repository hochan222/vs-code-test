word = input()
for k in range(ord('a'), ord('z')+1):
    print(word.find(chr(k)))
