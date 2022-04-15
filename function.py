#Parameterless function defination
def greeting():
    print("Hello user")
    print('Welcome to Abroad')

print("START")
greeting()
print("END")

#Parameter function

def greet_user(name, programming):
    print(f'Hello, {name}')
    print(f'Welcome to {programming} language')

greet_user('Nirajan','Python')


#Demo
Full_name=input("Enter your name : ")
lang=input("Enter your favrout programming language : ")
name=Full_name.split()
greet_user(name[-1],lang)