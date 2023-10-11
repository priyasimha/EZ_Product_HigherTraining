target=int(input())
lst=list(map(int,input().split()))
flag=0
for i in range(len(lst)):
    if target==lst[i]:
        flag=1

if flag==1:
    print("Element Found",[i])
else:
    print("Element Not Found")
