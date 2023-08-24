with open('rosalind_ini3.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

    sentence = lines[0]
    numbers = lines[1]

    a,b,c,d = numbers.split(' ')

    print(sentence[int(a):int(b)+1], sentence[int(c):int(d)+1])

