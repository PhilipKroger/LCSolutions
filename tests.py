n = 9
st = []
for i in range(2, n-1):
    l = ''
    nd = n
    while nd > 0:
        l += str(nd%i)
        nd = nd//i
    st.append(l)
    l = ''
ln = 0
for i in range(len(st)):
    c = st[i]
    if c == c[::-1]:
      ln += 1
if ln == len(st):
    print(True)
else:
    print(False)