dataset = "GATGGAACTTGACTACGTAAATT"
rna = ""

for i in dataset:
    if i == "T":
        rna += "U"
    else:
        rna += str(i)
print(rna)

