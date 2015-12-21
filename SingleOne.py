n=int(input('Enter the size of array : '))
if(n%2==0):
    print('Size of array is even - Hence all element must appear twice according to given problem !')
else:
    arr=[]
    for i in range(n):
        arr.append(int(input('Enter the Element '+ str(i+1) + ': ' )))
    arr.sort()
    for i in range(0,n,2):
        #print(i)
        if(i!=(n-1)):
            if(not arr[i]==arr[i+1]):
                print(str(arr[i]) +' is that Single one ..')
                break;
        else:
            print(str(arr[i])+ ' is that Single one ..')
