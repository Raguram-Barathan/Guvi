a=map(int , list(raw_input().split()))
a.sort()
i=0
while i<len(a):
    if a[i]!=a[i+1]:
        print a[i]
        break
    i+=2
