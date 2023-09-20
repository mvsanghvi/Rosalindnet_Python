with open('rosalind_ini6.txt', 'r') as f:
    lis = [line.split(" ") for line in f.readlines()]
    print(lis)
    sortedout= lis.sort()
    print(sortedout)
    for key, value in sortedout.items():
        print(key)
        print (value)
    