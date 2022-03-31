is_month=input("Enter the month.")
summer=['May',"June",'July']
autom=['Agust','September','October']
winter=['November','December','January']
spring=['Feburary','March','April']

if is_month.title() in summer:
    print("This month is Summer month.")
elif is_month.title() in autom:
    print("This month is Autom month.")

elif is_month.title() in winter:
    print("This month is Winter month.")
elif is_month.title() in spring:
    print("This month is Spring month.")
else:
    print("Wrong entry.")

#Task By MOSH

price=1000000
good_credit=True
advance=0
if good_credit:
    advance=price*.1
    print("The advance payment is ",advance)
else:
    advance=price*.2
    print("The advance payment is ",advance)