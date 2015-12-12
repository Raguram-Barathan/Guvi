a=list(map(int , list(raw_input().split())))
t=int(raw_input())
x=range(len(a))
x.reverse()
for i in x:
    if t-a[i] in a:
        if a.index(t-a[i])!=i:
            print t-a[i]
            print a[i]
            break
