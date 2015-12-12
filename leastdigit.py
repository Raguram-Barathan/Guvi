n=input()
l=len(n)
k=int(input())
if(k>=l):
    print('wrong input')
else:
    nums=[]
    for i in n:
        nums.append(i)
    nums.sort()
    re=l-k
    new=0
    for i in range(re):
        new=new*10+int((nums[i]))
    print(new)
