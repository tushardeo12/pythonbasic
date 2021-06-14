inp=int(input("enter the element to check -"))
lst=[1,2,3,4,5,6,7,8,9,10]
flag=0
for i in lst:
    if i==inp:
        flag=1
        print(inp," is found in the list")
        break
if flag==0:
    print(inp,"not found in the list")