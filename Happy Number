n=int(input('Enter the number : '))
num=n
temp=[]
while(n!=1):
    tn=0
    t=str(n)
    for i in range(len(t)):
        tn=tn+int(t[i])*int(t[i])
    if(tn not in temp):
        temp.append(tn)
        n=tn
    else:
        print(str(num) + ' is not an Happy Number')
        break
else:
    print(str(num) +' is a Happy Number')
