## THhis programm gives the LCM of the TWO numbers take by the user

inp1=int(input("enter the 1st number  -"))
inp2=int(input("enter the 2nd number - "))
if inp1>inp2:
     greater = inp1
else :
    greater =inp2
    while(1):
        if((greater% inp1==0) and (greater %inp2 == 0)):
            LCM=greater
            break
        greater=greater+1
print("the LCM of ",inp1 ,"and",inp2,"is",LCM)






