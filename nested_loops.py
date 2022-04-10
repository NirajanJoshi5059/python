#Nested loop for 4*3 matrix

for i in range(4):
    for j in range(3):
        print(f"{i},{j}", end="  ")
    print('\n')

#Nested loop to create F shape

f_shape=[5,2,5,2,2]
# for i in f_shape:
#     print("X"*i)
for x_count in f_shape:
    count=''
    for cnt in range(x_count):
        count+='X'
    print(count)