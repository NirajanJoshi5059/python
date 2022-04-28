
rate=4
try:
    name=input("Enter your name : ")
    age= int(input("Enter your age : "))
    bank_bln=float(input("Enter your salary : "))
    print("Resource open")
    mnth_interest=bank_bln*(rate/100)
    print(mnth_interest)
except ZeroDivisionError as e:
    print("Cannot divide by zero", e)

except ValueError as e:
    print("Invalid value", e)
except Exception as e:
    print(e)

finally:
    print("Resource closed")
