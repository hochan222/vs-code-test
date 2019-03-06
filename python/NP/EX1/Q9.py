my_basket = ['clover', 'pansy', 'clover', 'rose', 'ivy', 'daisy']

counter = {}
for v in my_basket:
    if v in counter:
        counter[v] += 1
    else:
        counter[v] = 1
print(counter)
