#Reverse a list in python
from ctypes import cast
from operator import le


name=['Nirajan','Kiran','Bimal','Bhuwan','Saurav']
n=len(name)
rev=[]
for i in range(n-1, -1,-1):
    rev.append(name[i])
print(rev)
# name.reverse()
# print(name)#change the list order

#Concatenate two lists index-wise
#This program need exactly equal number of items in both list.
name=['Nirajan','Kiran','Bimal','Bhuwan','Roshika']
caste=['Joshi','Basnet','Poudel','Sharma','Shrestha']
# fullname=[i+" "+j for i, j in zip(name, caste) ]
# print(fullname)
full_name=[]
for i in range(len(name)):
    full_name.append(name[i]+caste[i])
print(full_name)


#Turn every item of a list into its square
num=[1,2,3,4,5,6]
sq=[]
# for i in range(len(num)):
#     sq.append(num[i]**2)
# print(sq)
for i in num:
    sq.append(i*i)
print(sq)


#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        res.append(list1[i]+list2[j])
print(res)

#Iterate both lists simultaneously  
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)
