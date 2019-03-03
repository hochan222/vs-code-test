while True:
    try:
        ip = str(input())
        if ip.startswith(' ') or ip.endswith(' '):
            break
        print(ip)
    except EOFError:
        break
