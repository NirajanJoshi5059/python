name_list=['Nirajan','Saurav','Jagat','Sristi','Sardha']
#To print first index first letter
print(name_list[0][0])
#To print third index of list
print(name_list[2])
#To print 2nd to 3rd item in list
print(name_list[2:4])
#To print all item after 2nd include 2nd item
print(name_list[2:])
#To print all item before 3rd
print(name_list[:3])


#To find greatest number in list

number=[10,95,58,75,489,358]
largest_number=number[0]
for i in number:
    if largest_number< i:
        largest_number=i
    
print(largest_number)


#Conver a list into list of dictionaries
li=['Nirajan',23,'Kiran',24,'Bimal',26,'Bhuwan',25]
key_list=['name','age']
print("Original list : ", li)
n=len(li)
res=[]
for xid in range(0,n,2):
    res.append({key_list[0] : li[xid], key_list[1] : li[xid+1]})

print("Final Dictionary : ", res)

