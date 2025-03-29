Pattern= "AAAACCCGGT"
rev= ""
for i in reversed(Pattern):
    rev += str(i)
print(rev)
# Copy your Complement() function here.
comp = ""
for i in Pattern:
    if i == "A":
        comp += str("T")
    elif i == "C":
        comp += str("G")
    elif i == "G":
        comp += str("C")
    elif i == "T":
        comp += str("A")
print(comp)