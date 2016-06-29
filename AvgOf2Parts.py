import statistics as s
n=list(map(int,list(input().split())))
nl=len(n)
s1=nl//2
c=0
if nl%2==0:
    c=1
while c<2:
    a1=n[0:s1]
    a2=n[s1:nl]
    if s.mean(a1)==s.mean(a2):
        print(a1,a2)
        break
    s1+=1
    c+=1
else:
    print ("not possible")
