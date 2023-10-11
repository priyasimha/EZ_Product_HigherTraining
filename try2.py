rows=int(input("enter the rows"))
columns=int(input("enter the columns"))
symbol=input("enter the symbol")
for x in range(rows):
    for y in range(columns):
        print(symbol,end="  ")
    print()
