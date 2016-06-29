n=list(map(int,list(input().split())))
n.sort()
i=0
while i<len(n)-1:
    if n[i]!=n[i+1]:
        print(n[i])
        break
    i=i+2
else:
    print(n[i])
