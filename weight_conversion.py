#Weight conversion from kilogram to pound and viceversa.
weight=int(input("Enter your weight : "))
unit=input("Enter 'L' for pound and 'K' for kg. : ")
#It means if you choose L your weight is in pound and viceversa.
converted=''

if unit.upper()=="L":
    converted=weight*.456

    print(f"Your weight is {converted} KG.")
elif unit.upper()=="K":
    converted=weight/.456
    print(f"Your weight is {converted} Pounds.")
else:
    print("You have choose wrong letter.")

