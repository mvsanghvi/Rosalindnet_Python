def odd_sum(a, b):
    total = 0
    if a % 2 == 1:
        a = a+2
        total += a
        if a == b:
            print(total)
            break
    else:
        a = a+1
        if a % 2 == 1:
            a = a+2
            total += a
            if a == b:
                print(total)
                break
        