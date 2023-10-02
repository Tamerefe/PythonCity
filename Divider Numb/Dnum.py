num = 14629

prfd = 1

while num >= 10:

    print(num)
    prf = num % 10
    num = num // 10

    prfd *= prf

    if num < 10:
        num = prfd
        prfd = 1