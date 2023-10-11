def twosum(nums,tar):
    t=tar
    indi=[]
    while t!=0:
        for i in range(len(nums)):
            t = t-nums[i]
            indi.append(i)
            if t==0:
                break
            elif t<0:
                    t=tar
                    
    return indi
nums = list(map(int,input().split()))
tar=input()
k=twosum(nums,tar)
print(k)