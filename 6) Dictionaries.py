from collections import Counter
with open('rosalind_ini6.txt', 'r') as f:
    # lis = [line.split(" ") for line in f.readlines()]
    # print(lis)
    # sortedout= lis.sort()
    # print(sortedout)
    lns= f.readlines()
    print(lns)
    print(type(lns))
    lis = lns[0].split(" ")
    print(lis)
    lis.sort()
    print(lis)
    print(type(lis))
    # for word in lis:
    #     print(word)
    cnt= Counter(lis)
    print(cnt)
    for key in cnt:
        print(key, cnt[key])
    # print(type(cnt))
        
    # for key, value in lis.items():
    #     print(key)
    #     print (value)

#parce sentence into a list, count occurances