# code to print pallindrome number in a given range.
inp1 = int(input("enter the lower limit of the range -"))
inp2 = int(input("enter the upper limit of the range -"))

while inp1<=inp2:
    copy = inp1  # copy is made. copy should only be used for further changes bit the original variable should not be used.
    sum = 0

    while copy != 0: # copy is used for modification.
        rem = copy % 10
        sum = sum * 10 + rem
        copy=int(copy/10)

    if inp1 == sum: # original variable is used for comparison
        print(inp1)


    inp1=inp1+1


