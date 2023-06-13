s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

l = [''] * len(s)
for i in range(len(indices)):
    l[indices[i]] = s[i]
l = ''.join(l)
print(l)
