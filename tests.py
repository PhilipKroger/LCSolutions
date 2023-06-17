s = "babad"
ans = ''
for i in range(1, len(s) - 1):
    l, r = i, i
    while l <= r:
        if s[l] != s[r]:
            break
        if r - l + 1 > len(ans):
            ans = s[l:r + 1]
        l -= 1
        r += 1

    l, r = i, i + 1
    while l <= r:
        if s[l] != s[r]:
            break
        if r - l + 1 > len(ans):
            ans = s[l:r + 1]
        l -= 1
        r += 1
print(ans)
