import random
#default it choose number between 0 to 1
for i in range(3):
    print(random.random())

# randint function can give random value from specific range
for i in range(3):
    print(random.randint(100000,999999))

member=['Nirajan','Saurav','Kiran','Bhuwan','Bimal','Shekhar']
print(random.choice(member))