# 어렵다... 이해해야됭....
import math
s = ['  *   ', ' * *  ', '***** ']


def make_stars(shift):
    for i in range(len(s)):
        #print('3',s)
        s.append(s[i] + s[i])
        #print('4',s)
        s[i] = ' ' * shift + s[i] + ' ' * shift
        #print('5',s)


numb = int(input())

k = int(math.log(numb / 3, 2))
#print('1',s)
for i in range(k):
    make_stars(2 ** i * 3)
#print('2',s)
for i in range(len(s)):
    print(s[i])

