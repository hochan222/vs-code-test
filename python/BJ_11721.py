ip = str(input())
ip_length = len(ip)

for i in range(0, ip_length, 10):
    print(ip[i:i+10])

