# Problem

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

with open('rosalind_ini5.txt', 'r') as f:
    for i, line in enumerate(f, start=1):
        if i%2==0:
            print(i, line)
