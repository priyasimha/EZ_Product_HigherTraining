arr=[3,1,2,8,4,5,6]
n=len(arr)
for i in range(n):
    for j in range(n-i):
        if arr[j]>arr[j+i]:
            temp=arr[j+i]
            arr[j+i]=arr[j]
            arr[j]=temp
print(arr)
