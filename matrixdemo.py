n=int(input())
matrix=[]
for i in range(n):
    s=list(map(int,input().split()))
    matrix.append(s)


for i in range(n):
    for j in range(n):
        a=matrix[j][i]
        print(a)