"""
name less than 3 is short
name more than 50 is long
name is perfect
"""
name=input("Enter your name.")
if len(name) < 3:
    print("Name is too short.")
elif len(name)<=50 and len(name)>=3:
    print("Perfect name.")
elif len(name)>50:
    print("Name too long.")

