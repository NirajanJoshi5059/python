#For loop with string.
# name= input("Enter your name. ")
# for ch in name:
#     print(ch)

#For loop with list.
phone_no_list=[9847620206,9845007122,9826835932,9860181886,9844375899,9867773888]
for ph_no in phone_no_list:
    print(ph_no)

#For loop with list of string
name_list=["Nirajan",'Saurav']
for name in name_list:
    for char in name:
        print(char)
    print("\n")

#common for loop
#range function.
for num in range(10):
    print(num)
#range function with initial and end (range(start, end)).
for num in range(5,10):
    print(num)
# range function with initial, end and step (range(start, end, step)).
for num in range(5,10,2):
    print(num)

prices=[30,59,75,68]
total=0
for price in prices:
    total+=price
print("Total cost is ",total)