inp=int(input("enter the number to print fibonacci series upto -"))
i=0
j=0
first_term=0
second_term=1
while i<inp:
    if i==0:
        next_term = 0
    elif i==1:
        next_term=1
    else:
        next_term=first_term+second_term
        first_term=second_term
        second_term=next_term
    i=i+1

    while j<10:
        if j==next_term:
            print(j," is a fibonacci number")
        else:
            print(j," is not a fibonacci number")
        j=j+1
        break


