a=list(map(int , list(raw_input().split())))
for i in range(len(a)):
    if a.index(a[i])!=i:
        print a[i]
        break
