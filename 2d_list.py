matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
for rows in matrix:
    for item in rows:
        print(item)

#2 list using for loop
x=[[(i,j) for j in range(3)]for i in range(3)]
print(x)

rows=[]
columns=[]
for i in range(3):
    for j in range(3):
        columns+=(i,j)
print(columns)  
#    rows.append(columns)

# print(rows)