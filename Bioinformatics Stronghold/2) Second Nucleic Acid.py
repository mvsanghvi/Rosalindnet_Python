rna = ""

with open('rosalind_ini8.txt', 'r') as f:
    h= f.readlines()
    h=h[0]
    print(h)
    for i in h:
        if i == "T":
            rna += "U"
        else:
            rna += str(i)
print(rna)