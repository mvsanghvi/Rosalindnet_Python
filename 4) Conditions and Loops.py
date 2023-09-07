def odd_sum(a, b):
    total = 0
    for x in range(b-a):
        if a % 2 == 1:
            if a <= b:
                total += a
                a = a+2
            else:
                print(total)
                break
        else:
            a = a+1


odd_sum(4246, 8680)