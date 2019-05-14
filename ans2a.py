l=[5,6,3,8,6,2]

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp



print(l)        