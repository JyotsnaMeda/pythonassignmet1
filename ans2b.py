list=[0,1,3,6,8,14,35]
first=0
last=len(list)-1
search = 10

while first<=last:
    mid=(first+last) // 2
    if search==list[mid]:
        print("exists at",mid+1)
        break
    elif search>list[mid]:
        first=mid+1
    else:
        last=mid-1


if first>last:
    print("not found")