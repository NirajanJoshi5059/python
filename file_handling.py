name=input('Enter your name : ')
age=input("Age : ")
academic_background=input("Academic background : ")
#write method only takes string format 
tuple1=(name, age, academic_background)
#writing in a file
file1=open(name, 'w')
for data in tuple1:
    file1.write(data)


#fetching from a file

readf=open('noc', 'r')
for data in readf:
    print(data)

#we use rb wb ab for binary format file
