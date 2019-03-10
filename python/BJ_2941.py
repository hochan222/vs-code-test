import re
p = re.compile(r'c=|c-|dz=|d-|lj|nj|s=|z=|[a-z]')
print(len(p.findall(input())))
