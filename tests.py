arr = [1, 4, 2, 5, 3]

sm = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if len(arr[i:j+1])%2!=0:
            sm += sum(arr[i:j+1])
print(sm)