n=int(input())
for i in range(0,n,+1):
    for j in range(i):
        print(" ",end=" ") 
    print("*")
    for k in  range(n,-1):
        print(" ",end=" ")
    print("*")


        