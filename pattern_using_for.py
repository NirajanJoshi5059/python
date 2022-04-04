#For loop to creat simple pattern
for i in range(1,6):
    print("*"*i)

#For loop to create reverse pattern
for i in range(5,0,-1):
    print("*"*i)

#For loop to create number pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")