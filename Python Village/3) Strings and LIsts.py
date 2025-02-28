# Problem:

# Given: A string s of length at most 200 letters and four integers a, b, c and d.

# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b] and s[d] in our slice.

with open('rosalind_ini3.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

    sentence = lines[0]
    numbers = lines[1]

    a,b,c,d = numbers.split(' ')

    print(sentence[int(a):int(b)+1], sentence[int(c):int(d)+1])

