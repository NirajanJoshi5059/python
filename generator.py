#generator is used to fetch one by one data from list 
#yield keyword doesn't ternimate the block of code.
def gen():
    n=1
    while n<=10:
        yield n*n
        n+=1

values=gen()
for i in values:
    print(i)