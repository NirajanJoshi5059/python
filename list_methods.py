name_list=['Nirajan','Kiran','Roshika','Prajuna','Bhuwan']
phone_list=[9847620206,9860181886,9845007122,9829835932]
number=[5,14,17,10,19,15,3,10]

#append method adds new item in last position of the list.
phone_list.append(9844375899)
print(phone_list)

#insert method adds new item in user specific position.
#insert(position, value)
name_list.insert(1,'Saurav')
print(name_list)

#pop method remove the last item from the list
phone_list.pop()
print(phone_list)

#remove method remove the item by it's value.
number.remove(5)
print(number)

#index method gives the index value of item in list.
print(phone_list.index(9845007122))

#count method gives the integer value of the item present in list
print(number.count(10))

#sort method arrange the list in accending order.
num=number.sort()
print(num)

nums=[1,6,9,7,4,8,2,9,3,4,5,8]
nums.sort()
nums.reverse()
print(nums)

#list_method task
#remove dublicate items from the list
num=[3,5,8,7,9,1,4,5,45,6,8,1,5,8,9,1,4,85,1,5,6,7]
uniques=[]
for i in num:
    if i not in uniques:
        uniques.append(i)
print(uniques)