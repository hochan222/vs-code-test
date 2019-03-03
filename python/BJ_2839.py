ip = int(input())
three = 0
five = ip//5
ip %= 5

while five >= 0:
    if ip % 3 == 0:
        three = ip//3
        ip %= 3
        break
    five -= 1
    ip += 5
print(ip == 0 and (three + five) or -1)
