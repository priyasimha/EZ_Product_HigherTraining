def stack():
    stack=list
    return stack

stack=['(','{','[',']','}',')']

count=0

for i in stack:
    if stack[0]==stack[-1]:
        result="True"
    elif stack[1]==stack[2]:
        result="True"
    elif stack[3]==stack[3]:
        result="True"
    else:
        result="False"
print(result)
    
    
    
    

    