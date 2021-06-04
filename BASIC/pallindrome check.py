# code to check weather a number is pallindrome or not.
inp=int(input("enter a number to check weather its pallindrome or not-"))
copy=inp  # whenever we make a copy of a variable then always use the copy for further modification instead of the variable
sum=0
while copy!= 0:  # all modifications are done in copy instead of inp in(line 5 to 8)
    rem = copy % 10
    sum = sum * 10 + rem
    copy=int(copy/10)

if inp==sum: # use original variable to compare anything to.Don't use the copied variable made (line 3)
    print(inp,"is a pallindrome number")
else:

    print(inp,"is a NOT a pallindrome number")

