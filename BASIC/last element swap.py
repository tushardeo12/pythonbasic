# # non modifiable list
# user_list=[1,2,3,4,5,6,7,8,9,10]
# print("before swapping",user_list)
# temp=user_list[0]
# user_list[0]=user_list[9]
# user_list[9]=temp
# print("after swaping",user_list)

# modifiable list
user_list=[1,2,3,4,5,6,7,8,9,10,11]
size=len(user_list)
print("the list contains",size,"elements")
print("before swapping",user_list)
temp=user_list[0]
user_list[0]=user_list[size-1]
user_list[size-1]=temp
print("after swaping",user_list)