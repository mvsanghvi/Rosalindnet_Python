# Problem

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

#Test code:
# f= "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# a= 0
# b= 0
# c= 0
# d= 0
# for i in f:
#   if i == 'A':
#     a= a+1
#   elif i == 'C':
#     b= b+1
#   elif i == 'G':
#     c= c+1
#   else:
#     d= d+1

# print(f"{a} {b} {c} {d}")

#final answer:
with open('rosalind_dna.txt', 'r') as f:
  h= f.readlines()
  print(h)
  h=h[0]
  print(h)
  a= 0
  b= 0
  c= 0
  d= 0
  for i in h:
    if i == 'A':
        a= a+1
    elif i == 'C':
        b= b+1
    elif i == 'G':
        c= c+1
    elif i == 'T':
        d= d+1
print(f"{a} {b} {c} {d}")