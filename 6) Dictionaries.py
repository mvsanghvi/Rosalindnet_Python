# Problem:

# Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s, where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.

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
    lis2 = []
    for a in lis:
        if a.endswith("\n"):
            lis2.append(a.replace("\n", ""))
        else:
            lis2.append(a)
        
    print(lis2)
    # lis = [a.replace("\n", "") if a.endswith("\n") else a for a in lis]
    # lis.sort()
    # print(lis)
    # print(type(lis))
    # for word in lis:
    #     print(word)
    cnt= Counter(lis2)
    # print(cnt)
    for key in cnt:
        print(key, cnt[key])
    # print(type(cnt))
        
    # for key, value in lis.items():
    #     print(key)
    #     print (value)

#parce sentence into a list, count occurances