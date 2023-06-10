n = 521

s = 0
for i in range(len(str(n))):
    if i%2==0:
        s += int(str(n)[i])
    else:
        s += (-int(str(n)[i]))
print(s)