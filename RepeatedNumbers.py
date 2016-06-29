n=list(map(int,list(input().split())))
num=set(n)
for i in num:
    if n.count(i)>1:
        print(str(i)+' ',end="")
