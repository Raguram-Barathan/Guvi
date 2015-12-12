a=list(map(int , list(raw_input().split())))
out=[]
p=1
for i in a:
    p*=i
for i in a:
    out.append(int(p*i**-1))
print out
