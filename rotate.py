n=map(int,list(input("enter the elements").split()))
k=int(input("Enter the steps to rotate"))
for i in range(k):
    n.insert(0,n.pop())
print (n)
