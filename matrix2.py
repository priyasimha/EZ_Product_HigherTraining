arr=[3,1,2,8,4,5,6]
n=len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
print(arr)
