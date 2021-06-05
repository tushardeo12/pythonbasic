inp1=int(input("enter the index of element to swap -"))
inp2=int(input("enter the index of element to swap with -"))

lst=[1,2,3,4,5,6,7,8,9,10]
print("the list before swapping is-",lst)
temp=lst[inp1]
lst[inp1]=lst[inp2]
lst[inp2]=temp
print("the list after sapping is -",lst)
