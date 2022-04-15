from unicodedata import name


def cost_cal(total_cost, shipping_cost, discount):
    total_bill=(1-discount)*total_cost+shipping_cost
    print(f"Total bill is {total_bill}")
#keyword argument should behind the positional argument.
cost_cal(total_cost=50, discount=.05, shipping_cost=5)

full_name=input("Enter your full name : ").split()
lang=input("Enter your favrouit programming language : ")

def greet(first_name, last_name, lang):
    print(f"Hello, Mr. {last_name}")
    print(f'{first_name} you are welcome to {lang} programming language.')

greet(full_name[0],full_name[-1],lang=lang)
