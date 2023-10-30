from collections import Counter
with open('rosalind_ini6.txt', 'r') as f:
    # lis = [line.split(" ") for line in f.readlines()]
    # print(lis)
    # sortedout= lis.sort()
    # print(sortedout)
    # for key, value in sortedout.items():
    #     print(key)
    #     print (value)
    lns= f.readlines()
    print(lns)
    print(type(lns))
    lis = lns[0].split(" ")
    print(lis)
    lis.sort()
    print(lis)
    print(Counter(lis))

    # cnt = f.split( )
    # print(cnt)
#parce sentence into a list, count occurances