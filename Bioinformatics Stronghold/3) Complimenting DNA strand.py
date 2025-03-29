rev= ""
with open('rosalind_revc.txt', 'r') as f:
    h= f.readlines()
    h=h[0]
    print(h)
    for i in reversed(h):
        rev += str(i)
# Copy your Complement() function here.
comp = ""
for i in rev:
    if i == "A":
        comp += str("T")
    elif i == "C":
        comp += str("G")
    elif i == "G":
        comp += str("C")
    elif i == "T":
        comp += str("A")
print(comp)