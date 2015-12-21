s=list(map(str,list(input().split())))
o={}
for j in range(len(s)):
    d={}
    for i in s[j]:
    	if i not in d:
        	d[i]=1
    	else:
        	d[i]=d[i]+1
    o[s[j]]=max(d.values())
for i in o:
    if o[i]==max(o.values())and max(o.values())!=1:
        print (i)
        break
