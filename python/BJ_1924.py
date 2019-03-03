def cu(n):
    n %= 7
    return print(days[n])


month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day = 0

ip = list(map(int, input().split()))

if ip[0] == 1:
    day = ip[1] - 1
    cu(day)
else:
    for i in range(ip[0]-1):
        day += month[i]
    day += ip[1] - 1
    cu(day)


