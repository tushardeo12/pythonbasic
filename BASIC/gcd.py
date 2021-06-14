# code to ckeck GCD of  two numbers
inp1=int(input("enter the 1st number -"))
inp2=int(input("enter the 2nd number -"))
if inp1> inp2:
    greater=inp1
    smaller=inp2
else:
    greater=inp2
    smaller=inp1
while 1:


    a= greater%smaller

    if a==0:
        print(smaller,"is the GCD of",inp1,"and",inp2)
        break
    else:
        greater=smaller
        smaller=a