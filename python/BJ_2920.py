sound = input().split(' ')

if sound == sorted(sound):
    print('ascending')
elif sound[::-1] == sorted(sound):
    print('descending')
else:
    print('mixed')

